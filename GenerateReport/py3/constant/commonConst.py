#!/usr/bin/env python
# -*- coding:utf-8 -*-


class colNameConst(object):
    def __init__(self):
        ###########列名英文转换为中文，编号转换为中文##########
        self.nameMap = {
            # AllCity
            'city_name': '市', 'riskValueSum': '总风险值', 'veh_net': '车辆数'
            , 'po_amount': '超速次数', 'avg_po_amount': '超速车均次数', 'po_riskValue': '超速风险值'
            , 'fd_amount': '疲劳驾驶次数', 'avg_fd_amount': '疲劳驾驶车均次数', 'fd_riskValue': '疲劳驾驶风险值'
            , 'bt_amount': '夜间禁行次数', 'avg_bt_amount': '夜间禁行车均次数', 'bt_riskValue': '夜间禁行风险值'
            , 'veh_online': '上线车辆', 'line_rate': '上线率', 'line_riskValue': '上线率风险值'
            , 'qualifi_rate': '数据合格率', 'qualifi_riskValue': '数据合格率风险值'
            , 'draft_amount': '漂移车辆数', 'draft_rate': '漂移车辆率', 'draft_riskValue': '漂移风险值'
            , 'mileage': '有效里程', 'mileage_total': '总里程', 'mileage_rate': '轨迹完整率', 'mileage_riskValue': '轨迹完整率风险值'
            , 'alarm_ser_amount': '总报警数', 'alarm_ser_deal_amount': '报警处理次数', 'alarm_ser_rate': '报警处理率',
            'alarm_ser_riskValue': '报警处理率风险值'

            # OneCity
            , 'transport_mng_name': '运管所'
            , 'company_name': '企业'

        }
        self.numberMap = {

            11: '市', 12: '总风险值', 13: '车辆数'
            , 21: '超速次数', 22: '超速车均次数', 23: '超速风险值'
            , 31: '疲劳驾驶次数', 32: '疲劳驾驶车均次数', 33: '疲劳驾驶风险值'
            , 41: '夜间禁行次数', 42: '夜间禁行车均次数', 43: '夜间禁行风险值'
            , 51: '上线车辆', 52: '上线率', 53: '上线率风险值'
            , 61: '数据合格率', 62: '数据合格率风险值'
            , 71: '漂移车辆数', 72: '漂移车辆率', 73: '漂移风险值'
            , 81: '有效里程', 82: '总里程', 83: '轨迹完整率', 84: '轨迹完整率风险值'
            , 91: '总报警数', 92: '报警处理次数', 93: '报警处理率', 94: '报警处理率风险值'

            # OneCity
            , 101: '运管所', 102: '企业'
        }

        self.cityName2IdMap = {
            '南京': '5000001',
            '无锡': '5000002',
            '镇江': '5000003',
            '苏州': '5000004',
            '南通': '5000005',
            '徐州': '5000006',
            '盐城': '5000007',
            '扬州': '5000008',
            '泰州': '5000009',
            '常州': '5000010',
            '宿迁': '5000011',
            '淮安': '5000012',
            '连云港': '5000013',
            #同名
            '南京市': '5000001',
            '无锡市': '5000002',
            '镇江市': '5000003',
            '苏州市': '5000004',
            '南通市': '5000005',
            '徐州市': '5000006',
            '盐城市': '5000007',
            '扬州市': '5000008',
            '泰州市': '5000009',
            '常州市': '5000010',
            '宿迁市': '5000011',
            '淮安市': '5000012',
            '连云港市': '5000013'
        }


        self.cityId2NameMap = {
            '5000001': 'nanJing',
            '5000002': 'wuXi',
            '5000003': 'zhengJiang',
            '5000004': 'suZhou',
            '5000005': 'nanTong',
            '5000006': 'xuZhou',
            '5000007': 'yanCheng',
            '5000008': 'yangZhou',
            '5000009': 'taiZhou',
            '5000010': 'changZhou',
            '5000011': 'suQian',
            '5000012': 'huaiAn',
            '5000013': 'lianYunGang'
        }

    def getCityId2NameMap(self):
        return self.cityId2NameMap

    def getCityName2IdMap(self):
        return self.cityName2IdMap


    def getnameMap(self):
        return self.nameMap

    def getnumberMap(self):
        return self.numberMap


class quotaConst(object):
    def __init__(self):
        # 正反向指标列，dic {'依赖指标':'风险值'}
        # 反向指标，以及对应的可生成的风险值列名
        self.negativeQuota = \
            {
                'avg_po_amount': 'po_riskValue'
                , 'avg_fd_amount': 'fd_riskValue'
                , 'avg_bt_amount': 'bt_riskValue'
                , 'draft_rate': 'draft_riskValue'
            }

        # 正向指标
        self.positiveQuota = \
            {
                'qualifi_rate': 'qualifi_riskValue'
                , 'line_rate': 'line_riskValue'
                , 'mileage_rate': 'mileage_riskValue'
                , 'alarm_ser_rate': 'alarm_ser_riskValue'
            }

    def getnegativeQuota(self):
        return self.negativeQuota

    def getpositiveQuota(self):
        return self.positiveQuota
