<?php
$row = exec('ls -ls',$output,$error);
while(list(,$row) = each($output)){
echo $row, "<BR>n";
}
if($error){
echo "Error : $error<BR>n";
exit;
}
?>
