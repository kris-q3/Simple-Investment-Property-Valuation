# readme
# 这里的估值是对投资型房地产估值，特别是商业地产：写字楼、商铺
# 住宅类地产如果是刚需，且能有足够的现金流保障生活质量不下降是可以考虑的
# 估值考虑了物业费等成本


import numpy as np

# 输入参数
annual_rent = 24000  # 年租金
remaining_years = 35  # 房屋剩余年限
monthly_maintenance_fee = 120  # 每月物业费
discount_rate = 0.075  # 折现率 (一般取5-10%，均值7.5%）

# 计算年净收入
annual_maintenance_fee = monthly_maintenance_fee * 12
annual_net_income = annual_rent - annual_maintenance_fee

# 计算每年的现值
discounted_cashflows = [annual_net_income / (1 + discount_rate) ** year for year in range(1, remaining_years + 1)]

# 计算总现值（房屋合理估值）
house_value = sum(discounted_cashflows)

print(f"房屋的合理估值为: {house_value:.2f} 元")
