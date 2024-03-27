# JustForVoiceToText

基于LocalAI、简易的语音转文字工具，项目使用了模型、客户端分离模式，无需Python本地加载模型。

## 使用说明

⚠️本项目基于Python3，其他版本请自行测试。

### 模型部署阶段

1.[Docker部署本地模型服务](https://localai.io/docs/getting-started/run-other-models/)

`docker run -ti -p 8080:8080 localai/localai:v2.11.0-ffmpeg-core whisper-base`

**模型建议whisper-small起步，请根据机器配置具体分配**

2.[测试本地模型接口](https://localai.io/features/audio-to-text/)

`curl http://localhost:8080/v1/audio/transcriptions -H "Content-Type: multipart/form-data" -F file="@$PWD/gb1.ogg" -F model="whisper-1"`

**前两步摘自官方文档，点击小标题可跳转**

### 代码调试阶段

3.运行`pip install -r requirements.txt`安装依赖

4.修改源代码目录下`config/config.json`文件，将`client_url`和`model_name`修改为上述实际的接口地址和模型名称

5.运行`pyinstaller main.spec`可打包为Windows下的EXE可执行程序，`main_mac.spec`对应MacOS下可执行程序

### 已知问题

MacOS下界面显示异常，后续修复。