<?php

    if ($_SERVER["REQUEST_METHOD"]=="POST"){
        $username = $_POST["username"]; 

//        echo htmlspecialchars($username); 

        try {
            require_once "dbh.inc.php" ;

            $query = "INSERT INTO users (username, pwd, email) VALUES (?,?,?);";
            $stmt =  $pdo-> prepare($query); 
            $stmt -> execute([$username, "0000", "penguin@gmail.com"]); 

            $pdo=null; 
            $stmt = null; 
            header("Location: ../5_1_comment_.php"); 
            die() ; 
        }catch(PDOException $e){

            die("Query Fails: " .$e->getMessage()); 
        }
    }else {
        header("Location: ../5_signup.php"); 
    }


?> 
