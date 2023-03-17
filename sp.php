<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Sysma - Shop</title>
    <link rel="stylesheet" href="product.css">
</head>
<?php
    $conn = mysqli_connect("127.0.0.1", "root", "", "demo") or die("Connection failed: ");
    $prod_id = $_GET['prod_id'];
    //$prod_id = 5;
    $sql = "SELECT * FROM product2 WHERE prod_id='$prod_id'";
    $result = mysqli_query($conn,$sql);
    if (mysqli_num_rows($result)>0) {
        while($row = mysqli_fetch_array($result)) {
            $prod_id=$row['prod_id'];
            $prod_name=$row['prod_name'];
            $item=$row['item'];
            $price=$row['price'];
            $stock=$row['stock'];
            $description=$row['description'];
        }
    } 
    else {
        echo "Không tìm thấy bản ghi nào";
    }
?>
<body>
    <header>
        <a href="#"><img src="2.png" class="logo" alt=""></a>
        <div class="title">
        </div>
    </header>
    <div>
        <div class="imgage_product">
            <a href="#"><img src="a5.jpg" class="mi_hai_tom" id="myImg" alt=""></a>
        </div>
        <div class="infor">
            <ul class="menu">
                <li><a href="">Sản phẩm</a></li>
                <li><a class="Price" href="">Price</a></li>
                <li><a href="">Stock</a></li>
                <button class="button">❤️</button>
            </ul>

            <ul class="menu_noidung">
                <li><a href=""><?php echo $prod_name; ?></a></li>
                <li><a class="Price" href=""><?php echo $price ?> VND/<?php echo $item ?> </a></li>
                <li><a href=""><?php echo $stock ?> <?php echo $item ?></a></li>
                <button class="button" onclick="markLocation()">Location</button>
            </ul>
        </div>
    </div>
    <div class="Description">
        <h2>
            Description:
        </h2>
        <h3>
            <?php echo $description ?>
        </h3>
        <!-- <a href=""><img src="image/to_mi.jpg" class="to_mi" alt=""></a> -->
        
    </div>


    
</body>
<script>
    var prod_id = "<?php echo $prod_id; ?>"; 
    var imagePath = "image/" + prod_id + ".jpg";
    var img = document.getElementById("myImg");
    img.src = imagePath;
    
    function goBack(){
        location.href='index.php';
    }
    function markLocation() {
        var url = './map?prod_id=' + <?php echo $prod_id?>;
        location.href=url;
    }
</script>
</html>