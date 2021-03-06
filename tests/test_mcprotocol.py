import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
import struct

import mcprotocol
from mcprotocol import CpuType, Protocol
from mcprotocol.fxdevice import FxDevice, FxDataType


# この様に設定する
mcprotocol.config.DESTINATION_IP = '192.168.1.15'
mcprotocol.config.DESTINATION_PORT = 6001
mcprotocol.config.PROTOCOL = Protocol.TCP_IP

# CPU 毎に通信プロトコルが異なるので、
# クラス生成時に CPU情報を入れる事でプロトコル判断を行う
mc_proc = mcprotocol.MCProtocol(cpu_type= CpuType.FX5UCPU)


# 単一デバイスの読み書き
D100_16_rd = mc_proc.get_device('SD8010', FxDataType.Signed16)
R32767_16_rd = mc_proc.get_device('R32767', FxDataType.Signed16)
#M1_16_rd = mc_proc.get_device('M1', FxDataType.Signed16)

#single_16_rd = mc_proc.get_device('D100', FxDataType.Signed16)
#single_u32_rd = mc_proc.get_device('D102', FxDataType.Unsigned32)
#single_fl_rd = mc_proc.get_device('D104', FxDataType.Float)
#single_16_wr = mc_proc.set_device('D100', 123, FxDataType.Signed16)
#single_u32_wr = mc_proc.set_device('D102', 1234567, FxDataType.Unsigned32, )
#single_fl_wr = mc_proc.set_device('D104', 1234.56789, FxDataType.Float)


# ユニットバッファの読み書き
#unit_buff_rd = mc_proc.get_device('U1\\G70', FxDataType.Signed16)
#unit_buff_wr = mc_proc.set_device('U1\\G36674', 1, FxDataType.Signed16) 


# 連続デバイスの読み書き
test2_list_16_rd = mc_proc.get_device_list('D110', 4, FxDataType.Signed16)
#test2_list_u32_rd = mc_proc.get_device_list('D112', 4, FxDataType.Unsigned32)
#test2_list_fl_rd = mc_proc.get_device_list('D114', 4, FxDataType.Float)

#test2_listdev_wr = mc_proc.set_device_list('D110', [10,2.5,(2 ** 8)], FxDataType.Signed16)



#ランダムデバイスの読み書き
#dev_list = [
#    FxDevice('D100', FxDataType.Signed16),
#    FxDevice('D104', FxDataType.Unsigned32),
#    FxDevice('D108', FxDataType.Float),
#]
#test3_randomdev_rd = mc_proc.get_device_random(dev_list)

#dev_list = [
#    FxDevice('D100', FxDataType.Signed16, 100),
#    FxDevice('D104', FxDataType.Unsigned32, 20),
#    FxDevice('D108', FxDataType.Float, 2),
#]
#test3_randomdev_wr = mc_proc.set_device_random(dev_list)


#for dev in dev_list:
#    print(repr(dev))


