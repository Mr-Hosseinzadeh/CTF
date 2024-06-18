<?php
if (isset($_FILES['uploaded_file'])) {
    $file_name = $_FILES['uploaded_file']['name'];
    $file_type = $_FILES['uploaded_file']['type'];
    $file_tmp = $_FILES['uploaded_file']['tmp_name'];
    $file_size = $_FILES['uploaded_file']['size'];
    $type = explode(".",$file_name);
    $image_name = uniqid("image-").".".end($type);
    $upload_directory = 'uploads/';
    $upload_path = $upload_directory . $image_name;
    $allowedMimeTypes = ['image/jpeg', 'image/png', 'image/gif'];


    if ( $file_size > 200000) {
        echo("<script>alert('The file is big!
        It should be less than 200 KB');window.location=\"\"</script>");
        return;
    }
    elseif(!in_array($file_type, $allowedMimeTypes)){
        echo("<script>alert('The file type is not allowed!');window.location=\"\"</script>");
        return;
    }
    try {
        move_uploaded_file($file_tmp,$upload_path );
        echo "<img src=\"".$upload_path."\"><br><br><br>";
    } catch (Throwable $th) {
        echo "Error";
    }
}
?>

<form method="POST" enctype="multipart/form-data">
    <input type="file" name="uploaded_file">
    <input type="submit" value="Upload">
</form>