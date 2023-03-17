<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>SYSMA</title>
    <link rel="stylesheet" href="main.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.2.3/css/bootstrap.min.css" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.1/css/all.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css" integrity="sha512-qOA3/PwARfL1NYQyW8/c3qgT0fJN/DcQ2Z1mRvKGS69p14sDmNLiO/OU8fQiCCjYFt7D0tdyyh0ZzeNv1B2iQQ==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <script src="https://cdn.jsdelivr.net/npm/p5@latest/lib/p5.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/p5@latest/lib/addons/p5.dom.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/ml5@latest/dist/ml5.min.js"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.3/jquery.min.js"></script>

</head>
<body>
<div class="container">
    <div class="row">
        <div class="logo"><a href="main.html"><img src="2.png" alt="icon1" width="80px" height="80px" class="img1" class="col-md-12 col-xs-12 col-sm-12"></a></div>
        <br>
        <div class="column column-left" class="myDiv">
            <h2>Tìm kiếm</h2>
            <div class="recomend-box">"Phô mai Con bò cười."</div>
            <div class="recomend-box">"Bánh khoai tây Lays."</div>
            <div class="recomend-box">"Xúc xích Ponnie."</div>
        </div>
        <div class="column" class="myDiv">
            <h2>Tìm đường</h2>
            <div class="recomend-box">"Gian hàng bánh kẹo nằm ở đâu?"</div>
            <div class="recomend-box">"Chỉ đường đến gian hàng đồ gia dụng."</div>
            <div class="recomend-box">"Ở đâu có bán thực phẩm chức năng?"</div>
        </div>
        <div class="column column-right" class="myDiv">
            <h2>Đề xuất</h2>
            <div class="recomend-box">"Sữa giúp tăng chiều cao."</div>
            <div class="recomend-box">"Thực phẩm tốt cho sức khỏe mẹ bầu."</div>
            <div class="recomend-box">"Thức uống tăng sức đề kháng."</div>
        </div>
    </div>

    <!-- search -->
    <div class="input-container">
        <form>
            <div class="search-container">
                <input type="text" placeholder="Tìm kiếm..." name="fullname" id="fullname">
                <button class="button"id="cam"  type="button">
                    <i class="fas fa-camera"></i>
                </button>
                <button class="button"id="voice" onclick="voice()" type="button">
                    <i class="fas fa-microphone"></i>
                </button>
            </div>
            <button type="button" id="btn">Tìm ngay<i class="fa fa-search"></i></button>
        </form>
        <button id="start-button" style="display:none;">Start</button>
        <div id="result"></div>
        <br/>
        <p>Powered by AlphaSolution</p>
    </div>
</div>
    <script src="cam.js"></script>
</body>
</html>