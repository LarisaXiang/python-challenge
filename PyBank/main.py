import os
import csv

def analyse_budget_data(filename):
    # 初始化变量
    months = []
    profit_losses = []

    # 读取CSV文件并提取数据
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # 跳过标题行

        for row in reader:
            # 提取日期和利润/损失数据
            date = row[0]
            profit_loss = int(row[1])

            months.append(date)
            profit_losses.append(profit_loss)

    # 计算总月数
    total_months = len(months)

    # 计算总利润/损失
    total_profit_losses = sum(profit_losses)

    # 计算利润/损失变化
    changes = [profit_losses[i] - profit_losses[i-1] for i in range(1, len(profit_losses))]

    # 计算平均变化
    average_change = sum(changes) / len(changes)

    # 计算最大增益和最大损失
    max_increase = max(changes)
    max_increase_date = months[changes.index(max_increase) + 1]  # 对应的日期是当前变化的下一个月份
    max_decrease = min(changes)
    max_decrease_date = months[changes.index(max_decrease) + 1]  # 对应的日期是当前变化的下一个月份

    # 输出结果
    print("Financial Analysis")
    print("-------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit_losses}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: {max_increase_date} (${max_increase})")
    print(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})")

# Example usage
filename = 'Resources/budget_data.csv'  # Replace with your actual filename
analyse_budget_data(filename)