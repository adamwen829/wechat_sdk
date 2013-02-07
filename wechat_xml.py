textResp = '<xml>\n\
                <ToUserName><![CDATA[%s]]></ToUserName>\n\
                <FromUserName><![CDATA[%s]]></FromUserName>\n\
                <CreateTime>%d</CreateTime>\n\
                <MsgType><![CDATA[text]]></MsgType>\n\
                <Content><![CDATA[%s]]></Content>\n\
                <FuncFlag>%d</FuncFlag>\n\
           </xml>'

picItem = '<item>\n\
            <Title><![CDATA[%s]]></Title>\n\
            <Description><![CDATA[%s]]></Description>\n\
            <PicUrl><![CDATA[%s]]></PicUrl>\n\
            <Url><![CDATA[%s]]></Url>\n\
           </item>\n'

picResp = '<xml>\n\
            <ToUserName><![CDATA[%s]]></ToUserName>\n\
            <FromUserName><![CDATA[%s]]></FromUserName>\n\
            <CreateTime>%d</CreateTime>\n\
            <MsgType><![CDATA[news]]></MsgType>\n\
            <Content><![CDATA[%s]]></Content>\n\
            <ArticleCount>%d</ArticleCount>\n\
            <Articles>\n\
            %s\n\
            </Articles>\n\
            <FuncFlag>%d</FuncFlag>\n\
           </xml> '
