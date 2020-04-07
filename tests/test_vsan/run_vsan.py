from mdslib.switch import Switch
import unittest

import logging
logging.StreamHandler().setLevel(logging.CRITICAL)
logging.getLogger().addHandler(logging.FileHandler("test_vsan.log"))

import json
with open('../credentials.json', 'r') as j:
		json_data = json.load(j)

user = json_data['username']
pw = json_data['password']
ip_address = json_data['ip_address']

p = 8443
sw = Switch(ip_address=ip_address,username=user,password=pw,connection_type='https',port=p,timeout=30,verify_ssl=False)

default_id = 1
boundary_id = [0,4095]
reserved_id = [4079,4094]
vsan_id = [2,3,4,5,6,7,8,9,10,11,4090,4091,4092,4093]


from test_vsancreate import *
TestVsanCreate.switch = sw
TestVsanCreate.create_id = vsan_id[10]
TestVsanCreate.boundary_id = boundary_id
TestVsanCreate.reserved_id = reserved_id
TestVsanCreate.max_vsan_fail = range(2, 256)
TestVsanCreate.max_vsan_success = range(2, 255)
TestVsanCreate.create_multiple_id = vsan_id[11]

from test_vsandelete import *
TestVsanDelete.switch = sw
TestVsanDelete.delete_id = vsan_id[12]
TestVsanDelete.default_id = default_id
TestVsanDelete.nonexisting_id = vsan_id[13]
TestVsanDelete.boundary_id = boundary_id
TestVsanDelete.reserved_id = reserved_id

from test_vsanaddinterfaces import *
TestVsanAddInterfaces.switch = sw
TestVsanAddInterfaces.vsan_id = [i for i in range(2,22)]
TestVsanAddInterfaces.fc_name = ['fc1/'+str(i) for i in range(31,49)] 
TestVsanAddInterfaces.pc_id = [i for i in range(247,257)]
TestVsanAddInterfaces.invalid_fc = ["fc2/1"]

from test_vsanattrid import *
TestVsanAttrId.switch = sw
TestVsanAttrId.vsan_id = vsan_id[9]
TestVsanAttrId.boundary_id = boundary_id
TestVsanAttrId.reserved_id = reserved_id

from test_vsanattrstate import *
TestVsanAttrState.switch = sw
TestVsanAttrState.vsan_id = vsan_id

from test_vsanattrinterfaces import *
TestVsanAttrInterfaces.switch = sw
TestVsanAttrInterfaces.vsan_id = vsan_id
TestVsanAttrInterfaces.fc_name = ["fc1/47","fc1/48"]

from test_vsanattrname import *
TestVsanAttrName.switch = sw
TestVsanAttrName.vsan_id = vsan_id
TestVsanAttrName.boundary_id = boundary_id
TestVsanAttrName.reserved_id = reserved_id
TestVsanAttrName.max32_name = "12345678912345678912345678912345"
TestVsanAttrName.beyondmax_name = "123456789123456789123456789123456"
TestVsanAttrName.repeated_name = "VSAN0001"
TestVsanAttrName.specialchar_name = "vsan?"   

from test_vsanattrsuspend import *
TestVsanAttrSuspend.switch = sw
TestVsanAttrSuspend.vsan_id = vsan_id
TestVsanAttrSuspend.boundary_id = boundary_id
TestVsanAttrSuspend.reserved_id = reserved_id

suite = unittest.TestLoader().discover('.','test_vsan*.py')
unittest.TextTestRunner(verbosity=2).run(suite)

'''
#
suite = unittest.TestLoader().discover('.',pattern='test_vsanattr*.py')
#
suite = unittest.TestLoader().loadTestsFromModule(test_vsancreate)
#
suite = unittest.TestLoader().loadTestsFromTestCase(TestVsanCreate)
#
suite = unittest.TestLoader().loadTestsFromNames(['test_vsancreate.TestVsanCreate.test_create_success','test_vsancreate.TestVsanCreate.test_create_boundary'])
#
tests = ['test_create_success',
'test_create_boundary',
'test_create_reserved',
'test_create_max_vsans_fail',
'test_create_max_vsans_success',
'test_create_samevsan_multipletimes']
suite = unittest.TestSuite(map(TestVsanCreate, tests))
'''
