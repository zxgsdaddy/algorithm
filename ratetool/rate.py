#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Damon"
# Date: 2019/12/10

def repaymentsPerM(principal, annual_rate, total_month):
    '''
    :param principal: 本金
    :param annual_rate: 年利率
    :param total_month: 总还款月数
    :return: 每月还款额
    '''
    monthly_rate = annual_rate / 12
    return principal * (monthly_rate * (1 + monthly_rate) ** total_month) / ((1 + monthly_rate) ** total_month - 1)


def repaymentRatePerM(principal, annual_rate, total_month, month):
    '''
    :param month: 还款月序号
    :return: 月归还利息
    '''
    monthly_rate = annual_rate / 12
    return principal * monthly_rate * ((1 + monthly_rate) ** total_month - (1 + monthly_rate) ** (month - 1)) / (
            (1 + monthly_rate) ** total_month - 1)


def repaymentPrincipalPerM(principal, annual_rate, total_month, month):
    '''
    :param month: 还款月序号
    :return: 月归还本金
    '''
    monthly_rate = annual_rate / 12
    return principal * monthly_rate * (1 + monthly_rate) ** (month - 1) / ((1 + monthly_rate) ** total_month - 1)


def total_rate(principal, annual_rate, total_month):
    '''
    :return: 总利息
    '''
    repayment_per_month = repaymentsPerM(principal, annual_rate, total_month)
    total_repayment = repayment_per_month * total_month
    total_rate = total_repayment - principal
    print("等额本息 贷款总额 %s 每月归还 %s " % (principal, repayment_per_month))
    print("总共还款 %s 总利息 %s" % (total_repayment, total_rate))
    return total_rate


def total_payment(principal, annual_rate, total_month, month):
    total_rate = 0
    total_principal = 0
    for m in range(month):
        total_rate += repaymentRatePerM(principal, annual_rate, total_month, m + 1)
        total_principal += repaymentPrincipalPerM(principal, annual_rate, total_month, m + 1)
    print("等额本息 第%s个月 总共归还利息%s 本金%s " % (month, total_rate, total_principal))
    return total_principal


def cal(money, proportion, Benchmark_rate, float_rate, total_month):
    '''
    :param money: 可使用资金
    :param proportion: 首付比例
    :param float_rate:  利率上浮
    '''
    total_price = money / proportion
    rate = Benchmark_rate * (1 + float_rate)
    print("首付款%s 首付比率%s 利率 %s" % (money, proportion, str(rate * 100) + "%"))
    print("可购买房屋总价上限 %s 按 %d 年分期计算" % (total_price, total_month / 12))
    total_rate(total_price - money, rate, total_month)


def buy(money, loan_life):  # 计算 首套 和 二套的情况
    print("可使用资金 %s" % money)
    print("二套".center(30, "-"))
    cal(money, 0.7, 0.048, 0.25, loan_life * 12)
    print("".center(30, "-"))
    cal(money, 0.6, 0.048, 0.25, loan_life * 12)
    print('首套'.center(30, "-"))
    cal(money - 50 * 10000 + total_payment(50 * 10000, 0.048 * (1 + 0.05), 30 * 12, 12 * 2), 0.3, 0.048, 0.2,
        loan_life * 12)


# flag = True
# while (flag):
#     print("请输入可用于购房的资金(万元)")
#     m = float(input(">>>"))
#     print("贷款年限")
#     y = int(input(">>>"))
#     buy(m * 10000, y)
#     print("")
#     flag = input("按n/N退出或继续").lower() != "n"
#     print("")


# cal(70 * 10000, 70 / 110, 0.0325, 0.1, 20 * 12)
cal(70 * 10000, 70 / 110, 0.048, 0.2, 20 * 12)
