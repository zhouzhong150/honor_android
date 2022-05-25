from honor_android.util.file_util import FileUtil

len = 5
url_list = []
merge_data = []
count = 0
du_count = 0

for i in range(len):
    now = i + 20
    file = 'android_issuetracker_{}_html.jl'.format(now)
    data = FileUtil.load_data_list(file)
    for data_ in data:
        url = data_.get('url')
        if url not in url_list:
            url_list.append(url)
            merge_data.append(data_)
            count = count + 1
            print('process count: ', count)
        else:
            du_count = du_count + 1
            print('process du_count: ', du_count)

FileUtil.write2jl(merge_data, 'android_issuetracker_html.jl')

data = FileUtil.load_data_list('android_issuetracker_html.jl')
for data_ in data:
    print(data_)
    break