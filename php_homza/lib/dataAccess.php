<?php

function initDb($table){
	$client = new couchClient('http://localhost:5984', $table);
	return $client;
}


function last_seen(){
	$db = initDb('inhabitants');
	
	$opts = array("descending" => true, "limit" => 30);
	$view = $db->setQueryParameters($opts)->getView('list' , "last_seen");

	return $view;
}


?>
