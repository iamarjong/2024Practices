<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h3> Comments</h3>  
    <form action = "includes/formhandler.inc1.php" method="post">
        <input type"text" name="username" placeholder="Comment"> 
        <button>Comment</button>
    </form>
    <br>
    <table>
        <?php             
            try {
                require_once "includes/dbh.inc.php" ;
                                
                $query = "SELECT * FROM users;";
                $stmt =  $pdo-> prepare($query); 
                $stmt -> execute(); 
                
                // $result = $stmt->fetch(PDO::FETCH_ASSOC); 
                // 這等同於讀取下一筆的意思
                
                $rows = array();
                while($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
                    $rows[] = $row;
                
                }   // reference: 
                    // https://stackoverflow.com/questions/12272017/returning-multiple-rows-with-mysqli-and-arrays 
                    // from https://stackoverflow.com/questions/32318108/select-multiple-rows-from-mysql
        

                $i = count($rows)-1 ; 
                // https://www.php.net/manual/en/function.count.php
                while ($i >=0 ){
                    // echo $rows[$i]["username"]. ",", count($rows);
                    echo "<tr><td>".$rows[$i]["username"]. "</td></tr>";

                    $i --;
                }
    
                $pdo=null; 
                $stmt = null; 
                die() ; 
            }catch(PDOException $e)  //  https://www.php.net/manual/en/language.exceptions.php
            {
                die("Query Fails: " .$e->getMessage()); 
            }
        ?> 
    </table> 

</body>
</html>
