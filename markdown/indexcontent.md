- [什么是灯海](#什么是灯海)
- [如何添加新页面](#如何添加新页面)
- [如何部署](#如何部署)
# 什么是灯海
[灯海]()又名[上海滩之王]()，是一个架空世界奇幻冒险系列。讲述了2012年世界末日之后上海滩的风云变幻。 \
~~你说得对，但上海滩之王是上海滩之王制作委员会自主研发的一款全新废土世界家族模拟角色扮演mod，在这里，割据一方的首领被称作军阀。你将扮演一名名为[Mr. Human]()的神秘角色，在废土中邂逅性格各异，能力各异的同伴们，与他们一起开枝散叶，开疆拓土，光复往日的荣光——同时逐步发掘[深渊]()的真相~~
# 如何添加新页面
1. 在[templates/index.html](templates/index.html)中添加对应页面的菜单并写在链接中写入url相对路径。这不是一个前端教程，网上的前端教程成千上万，这里就不加赘述了，就算您不懂这其中的原理，照猫画虎也能做。
2. 制作正文部分
    1. 编辑md格式文本，当然如果您不习惯可以跳过这一步直接制作html页面。这是一个忠告，使用markdown编写百科页面可以节省您无数的时间，而且做出来还好看。
    2. 你不需要手动输入目录，在vscode里面下载markdown all in one插件，按下[Ctrl]()+[Shift]()+[P]()，然后键入[Create Table of Contents]()就会自动根据标题生产目录。
    3. 在vscode里面下载markdown converter插件，打开md文件，在右键菜单中选择[Markdown PDF:Export(html)]()，就会在当前目录生成同名html文件。
    4. 把同名html文件里面body部分除script以外的标签全部复制下来。在template里面对应的目录下新建空白html文档，把刚才复制的内容粘贴进去。
    5. 在[httpservice.py]()中添加路由，使得点击导航栏的菜单能够转跳到对应页面。
3. 在页面内插入图片
    * 这里要注意，img标签后面的url是相对路径，譬如说你的页面url链接是[/background/apocalypse]()，虽然img里面的src属性写的是[logo.png]()，但是实际上链接到的是apocalypse同级，也就是[/background/logo.png]()。在[httpservice.py]()中添加路径为[/background/logo.png]()的路由，返回图片就可以了。
    * 你也可以将图片转换成base64字符串直接粘贴在html元素的属性里面，但不建议这样做，因为这会增加页面加载的时间。如果用上一种方法，用户可以先看到文字，后面等图片慢慢加载。除非你需要在多个不同的目录下使用同一张图片，譬如说页首的logo，这样的话就不需要给每个url目录单独写路由了。
# 如何部署
1. docker方式 \
把整个项目放到服务器上面，然后安装docker，执行[docker_build_and_run.sh]()脚本
2. 非docker方式 \
执行如下命令:
    ```bash
    gunicorn httpservice:app -c ./config.py
    ```
> 什么是docker？简单来说就是一个独立的环境，当然它不是虚拟机。您不用管它是什么！把它交给会搞服务器部署的人，他自然晓得是什么意思。实在想知道的话，到网上随便查一下[什么是docker](https://zhuanlan.zhihu.com/p/187505981)，就会有铺天盖地的文章和视频。