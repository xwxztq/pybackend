# pybackend


## 接口如下

模块名|链接地址|http请求方式|参数名|结果
---|:--:|:--:|:--:|---:
climax4music|ip地址/climaxs|POST|filepath|(st,ed)_(str格式) 
wav2mid|ip-address/wav2mids|POST|filepath,savepath(可选)|mid文件or文件路径？
genres|ip-address/genres|POST|filepath|向量or风格名称？
processions|ip-address/processions|POST|filename,minmain,maxmain,control,mild,savepath(可选)|mid文件or路径？
upload|ip-address/files/upload|POST|file|状态码以及结果
download|ip-address/files/download|GET|name|文件