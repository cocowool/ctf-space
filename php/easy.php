<?php
// 题目地址
//https://adworld.xctf.org.cn/challenges/details?hash=5e5ff94c-3a5a-11ed-abf3-fa163e4fa609&task_category_id=3
//
highlight_file(__FILE__);

$key1 = 0;
$key2 = 0;

//$a=1e9
$a = $_GET['a'];

//$b=000000000004qGUX
$b = $_GET['b'];

//$c='{"m":"2023abc", "n":[["1","2","3"],0]}';

// $a = "0e12346";
// $b = 200;
//echo(intval($a));

if(isset($a) && intval($a) > 6000000 && strlen($a) <= 3){
    if(isset($b) && '8b184b' === substr(md5($b),-6,6)){
        $key1 = 1;
        }else{
            die("Emmm...再想想");
        }
    }else{
    die("Emmm...");
}

$c=(array)json_decode(@$_GET['c']);
if(is_array($c) && !is_numeric(@$c["m"]) && $c["m"] > 2022){
    if(is_array(@$c["n"]) && count($c["n"]) == 2 && is_array($c["n"][0])){
        $d = array_search("DGGJ", $c["n"]);
        $d === false?die("no..."):NULL;
        foreach($c["n"] as $key=>$val){
            $val==="DGGJ"?die("no......"):NULL;
        }
        $key2 = 1;
    }else{
        die("no hack");
    }
}else{
    die("no");
}

if($key1 && $key2){
    include "Hgfks.php";
    echo "You're right"."\n";
    echo $flag;
}
