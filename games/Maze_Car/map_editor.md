# 迷宮製作教學

此文將會介紹如何使用`Tiled`這個軟體製作一個地圖，並放進[PAIA迷宮自走車](https://github.com/PAIA-Playful-AI-Arena/Maze_Car)中，讓我們的自走車可以跑在我們客製化的地圖。

建立好的地圖除了可以直接放入[PAIA迷宮自走車](https://github.com/PAIA-Playful-AI-Arena/Maze_Car)，在個人環境中做使用之外，也可以分享給其他人，讓所有人使用。

---

# 軟體安裝
    ⚙ 製作地圖需要安裝Tiled這個軟體，請大家到 [連結](https://www.mapeditor.org) 中下載適合自己電腦作業系統的版本：

## 安裝流程：

1. 進入到[官網](https://www.mapeditor.org)後點擊「Donload on itch.io」跳轉到下載頁面。
    ![](https://i.imgur.com/dCbcYXs.png)

    
    
2. 點擊「Download Now」後將會顯示捐款浮動視窗。
    ![](https://i.imgur.com/FAk59CN.png)

    
3. 點選最上方「No thanks, just take me to the downloads」的選項後，即可看到不同作業系統適用的安裝檔。
    ![](https://i.imgur.com/VUjvlKz.png)

    
4. 選擇與自己電腦相容的安裝檔即可下載並安裝。
    ![](https://i.imgur.com/OpnUnXD.png)

    

---

# 新增地圖專案
    ⚙ 這部分主要說明如何建立一個地圖檔案並儲存。



1. 開啟Tiled，建立新地圖
第一次開啟Tiled的時候，可以在左上角看到以下截圖畫面。其中紅框內是比較常用到的功能。
選擇「New Map」，進入到軟體中。
    ![](https://i.imgur.com/hvcCuC0.png)

    

    ---

1. 設定地圖大小
    
    選擇建立新地圖後會跳出地圖屬性設定視窗，其中「地圖大小」的設定將會直接影響迷宮大小。
    
    將「圖塊大小」的高與寬都調整回64px，並設定好地圖大小之後就可以按下「Save As」
    ![](https://i.imgur.com/gFWmHPO.png)


    ---

1. 儲存檔案
    
    存檔時需要注意存檔類型，預設為`.tmx`，也是Tiled可以直接打開編輯的檔案格式；而自走車使用的是JSON檔。
    
    這邊建議兩種檔案都儲存一個，避免後續想要修改之前設計的地圖時無法打開JSON檔案。
    
    ![](https://i.imgur.com/t7xnHam.png)

    

    ---

1. 新增圖塊集
    
    存好檔案之後就會進入到編輯頁面，其中右側是可以自由編輯的工具欄，我們會用到的只有紅色框框的「圖塊」區域，「圖層」與「物件」區域可以視個人需求所小或直接關閉。
    
    - 點選圖塊區域中間的「New Tileset」
        
      ![](https://i.imgur.com/g9yTAkG.png)

        
    - 在點擊「瀏覽」並打開[圖片檔](https://github.com/PAIA-Playful-AI-Arena/Maze_Car/blob/master/asset/tile.png?raw=true)。
        ![](https://i.imgur.com/nkzfo9h.png)

        ![](https://i.imgur.com/VcYvVEz.png)

        

- 將圖片寬度與高度調整為64px，邊距與間距分別為0px與0px。
    ![](https://i.imgur.com/VcASdqp.png)


- 成功新增圖庫集之後就可以開始編輯迷宮了
    ![](https://i.imgur.com/lvV0dAu.png)


---

# 編輯地圖


    ⚙ Tiled的基本編輯方式相當簡單，只需要使用滑鼠選取圖塊集的方塊，再移動到編輯區點擊方格即可。
    也可以持續按著滑鼠左鍵拖曳繪製
![](https://i.imgur.com/Qj4gktp.gif)



---

## 積木種類

圖塊集的每個格子都會有相對應的編號，其順序從1開始，由左至右、由上至下。

目前自走車使用到的編號為1~9，對應到的圖塊如圖所示，這9種圖塊的功能分別為：

1. 紅色方塊，普通牆面，不會移動
2. 黃色方塊，從起始位置向上來回移動的牆面
3. 綠色方塊，從起始位置向右來回移動的牆面
4. 藍色方塊，從起始位置向下來回移動的牆面
5. 紫色方塊，從起始位置向左來回移動的牆面
6. 自走車圖示，車子的起始位置
7. 終點位置
8. 旗子圖示，檢查點位置，用於計算未走出迷宮的玩家中誰走的有效距離較遠
9. 路障圖示，邊界點位置，車子若碰觸到則遊戲結束並視為未通關，通常用於有開放牆面的迷宮，以免玩家駛離迷宮區域

![](https://i.imgur.com/ppLiecU.png)

---

## 積木與地圖物件的關係

有些積木在轉換為實際迷宮物件的時候會佔據更多的空間，皆是以中心點向外展開。

1. 檢查點：實際大小為**3*3**
    
    編輯器
    ![](https://i.imgur.com/TWERgMY.png)

    實際地圖
    ![](https://i.imgur.com/0hcxMFU.png)


    
2. 終點：實際大小為**3*3**
    
    編輯器
    ![](https://i.imgur.com/I7dlcPc.png)
    
    實際範圍
    ![](https://i.imgur.com/v25Ir2j.png)

    
3. 自走車：實際大小為**2*2**
    
    編輯地圖時放置位置
    
    ![](https://i.imgur.com/3hVEBn5.png)

    
    實際範圍
    
    ![](https://i.imgur.com/oAQgSra.png)


---

## 常用工具與功能列

- 橡皮擦
    
    在上方工具列可以找到，使用方式與圖塊集相同。
    
    ![](https://i.imgur.com/8O9nkvX.png)

    
- 調整地圖大小
    
    在上方的選單選擇「地圖」→「調整地圖大小」
    
    可以調整當前地圖的長寬，並移動原先的地圖物件，在視窗中間將會出現預覽圖。
    ![](https://i.imgur.com/A1vp255.png)


---

# FAQ 與 注意事項

## 尺寸換算

在自走車遊戲中，地圖的一格牆壁換算迷宮內為5cm*5cm，因此如果想要製作寬度30cm的迷宮，在兩道牆中間需要留下6個空格。

    
![](https://i.imgur.com/JmUyfbc.png)


## 地圖長寬的規定

在開啟新地圖時需要設定地圖的寬度和高度，其中寬度與高度皆不能小於25。

需要注意的是，最右側一行的資料在自走車中並不會被讀取到，因此寬度需要多計算一行，並且不能放任何物件（放置等同無效）。

目前遊戲內的迷宮寬度為25cm(5格)，如果想要製作n*n格的迷宮，寬度設定為6n+2，高度為6n+1
![](https://i.imgur.com/33A4gJW.png)



## 地圖檔名如何命名

- 在`src`資料夾中找到`map`資料夾，將編輯好的`.json`檔放在此資料夾，需注意命名規則，檔名最後的數字就是地圖的編號。
    - 小試身手的地圖：level_`1`.json
    - 經典迷宮的地圖：normal_map_`1`.json
    - 移動迷宮的地圖：move_map_`1`.json
    
    ![](https://i.imgur.com/Djml1sE.png)

---