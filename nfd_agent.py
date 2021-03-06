'''
Copyright 2019 ykpark@dcn.ssu.ac.kr authors.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''

from concurrent import futures
import time
import socket
import logging
import subprocess
import re


import grpc

import nfd_agent_pb2
import nfd_agent_pb2_grpc
import ifaddr
import os
from cStringIO import StringIO

# http://snowdeer.github.io/python/2017/11/17/python-logging-example/
import logging
import logging.handlers
log = logging.getLogger('nfd_agent_log')
log.setLevel(logging.INFO)

formatter = logging.Formatter('[%(asctime)s][%(levelname)s](%(filename)s:%(lineno)d)> %(message)s')
fileHandler = logging.FileHandler('/root/logs/nfd_agent.log')
streamHandler = logging.StreamHandler()

fileHandler.setFormatter(formatter)
streamHandler.setFormatter(formatter)

log.addHandler(fileHandler)
log.addHandler(streamHandler)


_MIN_IN_SECONDS = 60
_ONE_DAY_IN_SECONDS = _MIN_IN_SECONDS * _MIN_IN_SECONDS * 24


def is_error(output_all):
    return ('Error' in output_all) or \
           ('cannot' in output_all) or \
           ('missing' in output_all) or \
           ('not found' in output_all) or \
           ('refused' in output_all)


class NFDRouterAgent(nfd_agent_pb2_grpc.NFDRouterAgentServicer):

    def NFDHostNotify(self, request, context):
        log.info("Agent Host Name  : %s" % request.name)
        log.info("Agent IP Address : %s" % request.ipaddr)
        log.info("Agent NIC Name : %s" % request.ifname)

        if len(request.host_adapters) > 0:
            for item in request.host_adapters:
                log.info("ipaddr=%s/%s, nicname=%s" 
                        % (item.nic_ipaddr,
                           item.nic_prefix,
                           item.nic_name))
        else:
            log.info("Use only one network!!!")

        return nfd_agent_pb2.AckReply(ack_code='%s' % 'ok')

    def NFDFaceList(self, request, context):
        # Get Face List
        cmd = "nfdc face list"
        if request.faceid > 0:
            cmd += (" | grep 'faceid=%s '" % request.faceid)
        ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        output_all = ps.communicate()[0]

        ack_reply = nfd_agent_pb2.AckReply()
        if is_error(output_all):
            ack_reply.ack_code = 'err'
            ack_reply.ack_msg = ('%s' % output_all)
            return nfd_agent_pb2.NFDFaceListRes(face=[], ack=ack_reply)
        else:
            ack_reply.ack_code = 'ok'

        output_all = output_all.replace(" re", "\tre")
        output_all = output_all.replace(" lo", "\tlo")
        output_all = output_all.replace(" co", "\tco")
        output_all = output_all.replace(" mt", "\tmt")
        output_all = output_all.replace(" ou", "\tou")
        output_all = output_all.replace(" fl", "\tfl")
        output_list = output_all.split("\n")
        
        faces = []
        for one_line in output_list:
            if one_line is None or one_line == '': continue
            item_list = one_line.split("\t")
            faceid, remote, local = ['','','']
            congestion, mtu, counters = ['','','']
            out, flags = ['','']

            for item in item_list:
                if 'faceid=' in item:
                    faceid = item[len('faceid='):]
                elif 'remote=' in item:
                    remote = item[len('remote='):]
                elif 'local=' in item:
                    local = item[len('local='):]
                elif 'congestion=' in item:
                    congestion = item[len('congestion='):]
                elif 'mtu=' in item:
                    mtu = item[len('mtu='):]
                elif 'counters=' in item:
                    counters = item[len('counters='):]
                elif 'out=' in item:
                    out = item[len('out='):]
                elif 'flags=' in item:
                    flags = item[len('flags='):]
                
            face = nfd_agent_pb2.NFDFace(
                        faceid      = faceid,
                        remote      = remote,
                        local       = local,
                        congestion  = congestion,
                        mtu         = mtu,
                        counters    = counters,
                        out         = out,
                        flags       = flags)
            faces.append(face)

        return nfd_agent_pb2.NFDFaceListRes(faces=faces, ack=ack_reply)

    def NFDFaceCreate(self, request, context):
        # nfdc face create remote udp://router.example.net
        # nfdc face create remote ether://[08:00:27:01:01:01] local dev://eth2 persistency permanent
        # nfdc face create remote udp://router.example.net reliability on
        # nfdc face create remote udp://router.example.net congestion-marking-interval 100 default-congestion-threshold 65536
        # nfdc face create remote udp://router.example.net congestion-marking off
        # nfdc face create remote udp://router.example.net mtu 4000
        cmd = "nfdc face create"
        if request.remote:
            cmd += (" remote %s" % request.remote)
        if request.persistency:
            cmd += (" persistency %s" % request.persistency)
        if request.local:
            cmd += (" local %s" % request.local)
        if request.reliability:
            cmd += (" reliability %s" % request.reliability)
        if request.congestion_marking:
            cmd += (" congestion_marking %s" % request.congestion_marking)
        if request.congestion_marking_interval:
            cmd += (" congestion_marking_interval %s" % request.congestion_marking_interval)
        if request.default_congestion_threshold:
            cmd += (" default_congestion_threshold %s" % request.default_congestion_threshold)
        if request.mtu:
            cmd += (" mtu %s" % request.mtu)
        
        ack_reply = nfd_agent_pb2.AckReply()
        if len(cmd) <= len('nfdc face create'):
            ack_reply.ack_code = 'err'
            ack_reply.ack_msg = 'subcommand is not set'
            return ack_reply
        
        ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        output_all = ps.communicate()[0]
        if is_error(output_all):
            ack_reply.ack_code = 'err'
            ack_reply.ack_msg = ('%s' % output_all)
        else:
            ack_reply.ack_code = 'ok'
            ack_reply.ack_msg = ('%s' % output_all)

        self.NLSRNeighborCreate(request)
        return ack_reply


    def NFDFaceDestroy(self, request, context):
        # nfdc face destroy [faceid]
        # Get Face List
        cmd = "nfdc face destroy"
        if request.faceid:
            cmd += (" %s" % request.faceid)
        
        ack_reply = nfd_agent_pb2.AckReply()
        if len(cmd) <= len('nfdc face destroy'):
            ack_reply.ack_code = 'err'
            ack_reply.ack_msg = 'faceid parameter is not set'
            return ack_reply
        
        ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        output_all = ps.communicate()[0]

        if is_error(output_all):
            ack_reply.ack_code = 'err'
            ack_reply.ack_msg = ('%s' % output_all)
        else:
            ack_reply.ack_code = 'ok'
            ack_reply.ack_msg = ('%s' % output_all)

        self.NLSRNeighborDelete(request)
        return ack_reply


    def NFDFibList(self, request, context):
        # Get Face List
        cmd = "nfdc fib list"
        if request.faceid > 0:
            cmd += (" | grep faceid=%s" % request.faceid)
        ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        output_all = ps.communicate()[0]

        ack_reply = nfd_agent_pb2.AckReply()
        if is_error(output_all):
            ack_reply.ack_code = 'err'
            ack_reply.ack_msg = ('%s' % output_all)
            return nfd_agent_pb2.NFDFibListRes(fib=[], ack=ack_reply)
        else:
            ack_reply.ack_code = 'ok'
        
        fib = []
        output_list = output_all.split("\n")
        for one_line in output_list:
            if not one_line or 'FIB:' in one_line: continue
            one_line = re.sub('^  /','/',one_line)
            fib.append(one_line)

        return nfd_agent_pb2.NFDFibListRes(fib=fib, ack=ack_reply)


    def NFDRouteList(self, request, context):
        cmd = "nfdc route list"
        if request.nexthop and request.nexthop != '0':
            cmd += (" nexthop %s" % request.nexthop)
        if request.origin:
            cmd += (" origin %s" % request.origin)
       
        ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        output_all = ps.communicate()[0]

        ack_reply = nfd_agent_pb2.AckReply()
        if is_error(output_all):
            ack_reply.ack_code = 'err'
            ack_reply.ack_msg = ('%s' % output_all)
            return nfd_agent_pb2.NFDRouteListRes(route=[], ack=ack_reply)
        else:
            ack_reply.ack_code = 'ok'
        
        route = []
        output_list = output_all.split("\n")
        for one_line in output_list:
            if not one_line or one_line == '': continue
            route.append(one_line)

        return nfd_agent_pb2.NFDRouteListRes(route=route, ack=ack_reply)


    def NFDRouteShow(self, request, context):
        # Get Face List
        cmd = "nfdc route show"
        if request.prefix:
            cmd += (" prefix %s" % request.prefix)
       
        ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        output_all = ps.communicate()[0]

        ack_reply = nfd_agent_pb2.AckReply()
        if is_error(output_all):
            ack_reply.ack_code = 'err'
            ack_reply.ack_msg = ('%s' % output_all)
            return nfd_agent_pb2.NFDRouteShowRes(route=[], ack=ack_reply)
        else:
            ack_reply.ack_code = 'ok'
        
        route = []
        output_list = output_all.split("\n")
        for one_line in output_list:
            if not one_line or one_line == '': continue
            route.append(one_line)

        return nfd_agent_pb2.NFDRouteShowRes(route=route, ack=ack_reply)


    def NFDRouteAdd(self, request, context):
        # nfdc route add prefix <PREFIX> nexthop <FACEID|FACEURI> [origin <ORIGIN>] [cost <COST>] [expires <EXPIRATION-MILLIS>]
        # nfdc route add prefix /localhost/nfd nexthop 257
        # nfdc route add prefix /localhost/nfd nexthop udp://192.168.123.123
        # nfdc route add prefix /localhost/nfd nexthop 257 cost 100
        cmd = "nfdc route add"
        if request.prefix:
            cmd += (" prefix %s" % request.prefix)
        if request.nexthop:
            cmd += (" nexthop %s" % request.nexthop)
        if request.origin:
            cmd += (" origin %s" % request.origin)
        if request.cost:
            cmd += (" cost %s" % request.cost)
        if request.expires:
            cmd += (" expires %s" % request.expires)
        
        ack_reply = nfd_agent_pb2.AckReply()
        if len(cmd) <= len('nfdc route add'):
            ack_reply.ack_code = 'err'
            ack_reply.ack_msg = 'subcommand is not set'
            return ack_reply
        
        ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        output_all = ps.communicate()[0]
        if is_error(output_all):
            ack_reply.ack_code = 'err'
            ack_reply.ack_msg = ('%s' % output_all)
        else:
            ack_reply.ack_code = 'ok'
            ack_reply.ack_msg = ('%s' % output_all)
        return ack_reply


    def NFDRouteRemove(self, request, context):
        # nfdc route remove prefix <PREFIX> nexthop <FACEID|FACEURI> [origin <ORIGIN>]
        # nfdc route remove prefix /localhost/nfd nexthop 257
        # nfdc route remove prefix /localhost/nfd nexthop udp://192.168.123.123
        # nfdc route remove prefix /localhost/nfd nexthop 257 origin static
        cmd = "nfdc route remove"
        if request.prefix:
            cmd += (" prefix %s" % request.prefix)
        if request.nexthop:
            cmd += (" nexthop %s" % request.nexthop)
        if request.origin:
            cmd += (" origin %s" % request.origin)

        ack_reply = nfd_agent_pb2.AckReply()
        if len(cmd) <= len('nfdc route remove'):
            ack_reply.ack_code = 'err'
            ack_reply.ack_msg = 'subcommand is not set'
            return ack_reply
        
        ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        output_all = ps.communicate()[0]

        if is_error(output_all):
            ack_reply.ack_code = 'err'
            ack_reply.ack_msg = ('%s' % output_all)
        else:
            ack_reply.ack_code = 'ok'
            ack_reply.ack_msg = ('%s' % output_all)

        return ack_reply


    def NFDStatusReport(self, request, context):
        cmd = "nfdc status report"
        if request.format:
            cmd += (" format %s" % request.format)
       
        ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        output_all = ps.communicate()[0]

        ack_reply = nfd_agent_pb2.AckReply()
        if is_error(output_all):
            ack_reply.ack_code = 'err'
            ack_reply.ack_msg = ('%s' % output_all)
            return nfd_agent_pb2.NFDStatusReportRes(report='', ack=ack_reply)
        else:
            ack_reply.ack_code = 'ok'

        # delete last \n character
        if request.format == 'text':
            if output_all.rindex('\n') > 0:
                output_all = output_all[::-1].replace('\n','',1)[::-1]

        return nfd_agent_pb2.NFDStatusReportRes(report=output_all, ack=ack_reply)


    def NFDStrategyList(self, request, context):
        cmd = "nfdc strategy list"
        ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        output_all = ps.communicate()[0]

        ack_reply = nfd_agent_pb2.AckReply()
        if is_error(output_all):
            ack_reply.ack_code = 'err'
            ack_reply.ack_msg = ('%s' % output_all)
            return nfd_agent_pb2.NFDStrategyListRes(strategies=[], ack=ack_reply)
        else:
            ack_reply.ack_code = 'ok'
        
        strategies = []
        output_list = output_all.split("\n")
        for one_line in output_list:
            if not one_line or one_line == '': continue
            strategies.append(one_line)

        return nfd_agent_pb2.NFDStrategyListRes(strategies=strategies, ack=ack_reply)


    def NFDStrategyShow(self, request, context):
        cmd = "nfdc strategy show"
        if request.prefix:
            cmd += (" prefix %s" % request.prefix)

        ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        output_all = ps.communicate()[0]

        ack_reply = nfd_agent_pb2.AckReply()
        if is_error(output_all):
            ack_reply.ack_code = 'err'
            ack_reply.ack_msg = ('%s' % output_all)
            return nfd_agent_pb2.NFDStrategyShowRes(strategy='', ack=ack_reply)
        else:
            ack_reply.ack_code = 'ok'

        # delete last \n character
        if output_all.rindex('\n') > 0:
            output_all = output_all[::-1].replace('\n','',1)[::-1]
        
        return nfd_agent_pb2.NFDStrategyShowRes(strategy=output_all, ack=ack_reply)


    def NFDStrategySet(self, request, context):
        # nfdc strategy set prefix <PREFIX> strategy <STRATEGY>
        # nfdc strategy set prefix /localhost strategy /localhost/nfd/strategy/best-route/%FD%05
        cmd = "nfdc strategy set"
        if request.prefix:
            cmd += (" prefix %s" % request.prefix)
        if request.strategy:
            cmd += (" strategy %s" % request.strategy)
        
        ack_reply = nfd_agent_pb2.AckReply()
        if len(cmd) <= len('nfdc strategy set'):
            ack_reply.ack_code = 'err'
            ack_reply.ack_msg = 'subcommand is not set'
            return ack_reply
        
        ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        output_all = ps.communicate()[0]
        if is_error(output_all):
            ack_reply.ack_code = 'err'
            ack_reply.ack_msg = ('%s' % output_all)
        else:
            ack_reply.ack_code = 'ok'
            ack_reply.ack_msg = ('%s' % output_all)
        return ack_reply

    def NFDStrategyUnset(self, request, context):
        # nfdc strategy unset prefix <PREFIX>
        # nfdc strategy set prefix /localhost
        cmd = "nfdc strategy unset"
        if request.prefix:
            cmd += (" prefix %s" % request.prefix)

        ack_reply = nfd_agent_pb2.AckReply()
        if len(cmd) <= len('nfdc strategy unset'):
            ack_reply.ack_code = 'err'
            ack_reply.ack_msg = 'subcommand is not set'
            return ack_reply
        
        ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        output_all = ps.communicate()[0]
        if is_error(output_all):
            ack_reply.ack_code = 'err'
            ack_reply.ack_msg = ('%s' % output_all)
        else:
            ack_reply.ack_code = 'ok'
            ack_reply.ack_msg = ('%s' % output_all)
        return ack_reply


    def NLSRNeighborCreate(self, request):
        if request.neighbor_hostname:
            file_str = StringIO()
            with open('/root/env_original', 'r') as f:
                for line in f:
                    n_hostname = "NEIGHBOR_HOSTNAME="
                    n_ip = "NEIGHBOR_IP="
                    n_siteroute = "NEIGHBOR_SITE_ROUTE="
                    strip_line = line.strip('\n')
                    file_str.write(strip_line)

                    if n_hostname in line:
                        #if len(n_hostname) != len(strip_line):
                        #    file_str.write(':')
                        file_str.write(request.neighbor_hostname)
                        file_str.write(':')
                    elif n_ip in line:
                        #if len(n_ip) != len(strip_line):
                        #    file_str.write(':')
                        file_str.write(request.neighbor_ip)
                        file_str.write(':')
                    elif n_siteroute in line:
                        #if len(n_siteroute) != len(strip_line):
                        #    file_str.write(':')
                        file_str.write(request.neighbor_site_route)
                        file_str.write(':')
                    file_str.write('\n')

            with open('/root/env_original', 'w') as fw:
                fw.write(file_str.getvalue())

            #cmd = "/root/start_vicsnf.sh"
            ps = subprocess.Popen(['/root/start_vicsnf.sh', 'grpc_nlsr'])
            #ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)

    def NLSRNeighborDelete(self, request):
        if request.neighbor_hostname:
            env_string = ''
            with open('/root/env_original', 'r') as f:
                env_string = f.read()
                if request.neighbor_hostname+':' in env_string:
                    env_string = env_string.replace(request.neighbor_hostname+':', '')
                elif ':'+request.neighbor_hostname in env_string:
                    env_string = env_string.replace(':'+request.neighbor_hostname, '')
                elif request.neighbor_hostname in env_string:
                    env_string = env_string.replace(request.neighbor_hostname, '')
                
                if request.neighbor_ip+':' in env_string:
                    env_string = env_string.replace(request.neighbor_ip+':', '')
                elif ':'+request.neighbor_ip in env_string:
                    env_string = env_string.replace(':'+request.neighbor_ip, '')
                elif request.neighbor_ip in env_string:
                    env_string = env_string.replace(request.neighbor_ip, '')
                    
                if request.neighbor_site_route+':' in env_string:
                    env_string = env_string.replace(request.neighbor_site_route+':', '')
                elif ':'+request.neighbor_site_route in env_string:
                    env_string = env_string.replace(':'+request.neighbor_site_route, '')
                elif request.neighbor_site_route in env_string:
                    env_string = env_string.replace(request.neighbor_site_route, '')
                
            with open('/root/env_original', 'w') as f:
                f.write(env_string)

            ps = subprocess.Popen(['/root/start_vicsnf.sh', 'grpc_nlsr'])


    def NLSRAdvertiseName(self, request, context):
        # nlsrc advertise or withdraw  <PREFIX> [option <save or delete>]
        cmd = "nlsrc"

        if request.mode:
            cmd += (" %s" % request.mode)
        if request.prefix:
            cmd += (" %s" % request.prefix)
        if request.save:
            cmd += (" %s" % request.save)

        ack_reply = nfd_agent_pb2.AckReply()
        if len(cmd) <= len('nlsrc advertise'):
            ack_reply.ack_code = 'err'
            ack_reply.ack_msg = 'subcommand is not set'
            return ack_reply
        
        ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        output_all = ps.communicate()[0]
        if is_error(output_all):
            ack_reply.ack_code = 'err'
            ack_reply.ack_msg = ('%s' % output_all)
        else:
            ack_reply.ack_code = 'ok'
            ack_reply.ack_msg = ('%s' % output_all)
        return ack_reply

    def NLSRLsdbList(self, request, context):
        # Get Face List
        cmd = "nlsrc lsdb"
        ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        output_all = ps.communicate()[0]

        ack_reply = nfd_agent_pb2.AckReply()
        if is_error(output_all):
            ack_reply.ack_code = 'err'
            ack_reply.ack_msg = ('%s' % output_all)
            return nfd_agent_pb2.NLSRLsdbListRes(lsdb=[], ack=ack_reply)
        else:
            ack_reply.ack_code = 'ok'
        
        lsdbs = []
        output_list = output_all.split("\n")
        origin_router = ''
        for one_line in output_list:
            if 'OriginRouter: ' in one_line:
                if origin_router == '' or origin_router not in one_line:
                    origin_router = re.sub('^  OriginRouter: ', '', one_line)
        
            if 'name=/' in one_line:
                one_line = re.sub('^      name=/', '/', one_line)
                lsdb = nfd_agent_pb2.LSDB(origin_router = origin_router,
                                          prefix    = one_line)
                lsdbs.append(lsdb)

        return nfd_agent_pb2.NLSRLsdbListRes(lsdbs=lsdbs, ack=ack_reply)


    def NFDDaemon(self, request, context):
        if request.opt == 'start':
            log.info("NFDDaemon Start")
        elif request.opt == 'stop':
            log.info("NFDDaemon stop")
        elif request.opt == 'restart':
            log.info("NFDDaemon restart")
        else:
            log.info("opt is not support")

    def NLSRDaemon(self, request, context):
        if request.opt == 'start':
            log.info("NLSRDaemon Start")
        elif request.opt == 'stop':
            log.info("NLSRDaemon stop")
        elif request.opt == 'restart':
            log.info("NLSRDaemon restart")
        else:
            log.info("opt is not support")


# Function to display hostname and
# IP address 
def get_Host_name_IP():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
    except:
        log.info("Unable to get Hostname and IP")
    return host_name, host_ip


def wait_on_client():
    try:
        while True:
            host_name, host_ip = get_Host_name_IP()
            if host_name is None or host_ip is None:
                time.sleep(_MIN_IN_SECONDS)
                continue
            break

        while True:
            mgmt_ip = os.getenv('vICSNF_MGMTIP', '127.0.0.1')
            mgmt_port = os.getenv('vICSNF_MGMTPORT', '50051')
            with grpc.insecure_channel('%s:%s' % (mgmt_ip, mgmt_port)) as channel:
                try:
                    grpc.channel_ready_future(channel).result(timeout=10)
                except grpc.FutureTimeoutError:
                    log.error("Unable connection to external server")
                    time.sleep(_MIN_IN_SECONDS)
                    continue
                stub = nfd_agent_pb2_grpc.NFDRouterAgentStub(channel)

                # https://pythonhosted.org/ifaddr/
                # all interface and ip address
                adapters = ifaddr.get_adapters()
                host_adapters = []
                for adapter in adapters:
                    if adapter.nice_name == 'lo': continue
                    for ip in adapter.ips:
                        if ip.ip == host_ip:
                            host_ifname = adapter.nice_name
                            break
                        elif '::' in ip.ip:
                            continue
                        else:
                            host_adapter = nfd_agent_pb2.HostAdapters(
                                            nic_ipaddr=ip.ip,
                                            nic_prefix=str(ip.network_prefix),
                                            nic_name=adapter.nice_name)
                            host_adapters.append(host_adapter)

                nfdhost = nfd_agent_pb2.NFDHost(
                    name=host_name,
                    ipaddr=host_ip,
                    ifname=host_ifname,
                    host_adapters=host_adapters)

                ack_reply = stub.NFDHostNotify(nfdhost)
                if ack_reply.ack_code is None or ack_reply.ack_code != 'ok':
                    continue
            log.info("NFDHostNotify is %s" % ack_reply.ack_code)
            break
    except KeyboardInterrupt:
        sys.exit('Error connecting to server')


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    nfd_agent_pb2_grpc.add_NFDRouterAgentServicer_to_server(NFDRouterAgent(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    logging.basicConfig()
    
    # NFD Informational notification thread
    client_thread = futures.ThreadPoolExecutor(max_workers=1)
    client_thread.submit(wait_on_client)

    serve()
