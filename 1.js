         //#endregion  //#region 1.js
            //#region 2.js
            //#endregion  //#region 2.js

            //取款 
            money = 10000000
            s=money.toString()
            if  (s.length>=4)
            {
                s=s.substr(0,s.length-4)+"."+s.substr(s.length-4,4)
            }
            else    
            {
                s="0."+s
            }
            document.getElementById("money").innerHTML=s
            document.getElementById("money").style.color="red"
            document.getElementById("money").style.fontSize="30px"
            document.getElementById("money").style.fontWeight="bold"
            document.getElementById("money").style.fontFamily="微软雅黑"
            document.getElementById("money").style.textAlign="center"
            document.getElementById("money").style.marginTop="20px"
            document.getElementById("money").style.marginBottom="20px"
            document.getElementById("money").style.marginLeft="20px"
            
