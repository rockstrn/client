# 命令行参数
### serverip
服务端口号server ip:port

### url
网络地址

### reqfile
请求文件 request file

### servers
请求的服务类型
图文策略 txt
图文召回 txt_recall
图文打分 txt_score
图文nn打分 txt_dnn_score

视频merger video_merger
短视频策略 video
短视频召回 video_recall
短视频打分 video_score
短视频fm打分 video_fm_score

小视频 tiny_video
小视频打分 tiny_video_score
小视频fm打分 tiny_video_fm_score

如 --servers txt 表示请求的服务为图文策略

### isbase64
请求服务需要的类型是不是base64类型程序,1代表是,0代表不是，默认为不是
