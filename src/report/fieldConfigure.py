# 字段

# 订单类型
OrderTypeDict = {
    'U': "未定义",
    '1': "市价单",
    '2': "限价单",
    '3': "市价止损",
    '4': "限价止损",
    '5': "行权",
    '6': "弃权",
    '7': "询价",
    '8': "应价",
    '9': "冰山单",
    'A': "影子单",
    'B': "互换",
    'C': "套利申请",
    'D': "套保申请",
    'F': "行权前期权自对冲申请",
    'G': "履约期货自对冲申请",
    'H': "做市商留仓"
}

# 有效类型
ValidTypeDict = {
    'N': "无",
    '0': '当日有效',
    '1': '长期有效',
    '2': '限期有效',
    '3': '即时部分',
    '4': '即时全部'

}

# 投保标记
HedgeDict = {
    'N': '无',
    'T': '投机',
    'B': '套保',
    'S': '套利',
    'M': '做市'
}

# 买卖
DirectDict = {
    'N': '',
    'B': '买',
    'S': '卖',
    'A': '双边'
}

# 开平
OffsetDict = {
    'N': '',
    'O': '开',
    'C': '平',
    'T': '平今',
    '1': '开平',
    '2': '平开',
}


# 周期
FrequencyDict = {
    'D': '日',
    'M': '分钟',
    'S': '秒'
}

# 策略状态
StrategyStatus = {
    'N':  '初始',
    'H':  '历史',
    'C':  '实盘',

    'P':  '暂停',
    'Q':  '停止',
    'R':  '移除',

    'E':  '异常'
}