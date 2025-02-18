import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 指定宋体字体文件路径
font_path = 'STHeiti Light.ttc'  # 根据你的系统路径进行调整

# 创建字体属性对象
font = FontProperties(fname=font_path, size=14)

# 岗位名称
labels = [
    '产品设计工程师', '工艺设计工程师', '数字化设备操作员', 
    '智能生产线现场管控员', '质量检测员', '三维造型师', 
    'CAE分析师', '数字化制造工艺设计及验证工程师', 
    '设备维修技术员', '生产管理员', '数字化设备技改技术员', 
    '数字化制造解决方案销售', '售后工程师', 
    '数字化资深工程师/专家', '智能制造产品经理'
]

# 用人比例
sizes = [
    12.5, 12.5, 25, 12.5, 12.5, 7.5, 7.5, 12.5, 12.5, 12.5, 7.5, 7.5, 7.5, 7.5, 7.5
]

# 生成饼状图
plt.figure(figsize=(10, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, textprops={'fontproperties': font})
plt.title('数字化设计与制造企业岗位群用人比例', fontproperties=font)
plt.axis('equal')  # 等轴比例
plt.show()