import pandas as pd

def main():
    # 读取数据
    data = pd.read_csv('iris.csv')
    # 过滤出品种为 setosa 的数据
    setosa_data = data[data['Species'] == 'setosa']

    # 计算花萼和花瓣的最小值、最大值和平均值
    results = []
    for column in ['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width']:
        mean_value = setosa_data[column].mean()
        min_value = setosa_data[column].min()
        max_value = setosa_data[column].max()
        if column == 'Sepal.Length':
            results.append(f'花萼长度平均值: {mean_value:.2f}, 最小值: {min_value:.2f}, 最大值: {max_value:.2f}')
        elif column == 'Sepal.Width':
            results.append(f'花萼宽度平均值: {mean_value:.2f}, 最小值: {min_value:.2f}, 最大值: {max_value:.2f}')
        elif column == 'Petal.Length':
            results.append(f'花瓣长度平均值: {mean_value:.2f}, 最小值: {min_value:.2f}, 最大值: {max_value:.2f}')
        else:
            results.append(f'花瓣宽度平均值: {mean_value:.2f}, 最小值: {min_value:.2f}, 最大值: {max_value:.2f}')
    # 将结果写入文件
    with open('result.txt', 'w') as f:
        f.write('\n'.join(results))


main()
