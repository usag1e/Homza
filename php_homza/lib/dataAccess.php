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

function get_url_img(){
	$db = initDb('inhabitants');
	
	$opts = array("descending" => true, "limit" => 30);
	$view = $db->setQueryParameters($opts)->getView('list' , "name_url_last_seen");

	return $view;
}

function get_printer_status(){
	$db = initDb('house_status');

	$opts = array("descending" => true, "limit" => 30);
	$view = $db->setQueryParameters($opts)->getView('list' , "printer");

	return $view;
}

function secondsToTime($seconds) {
    $dtF = new DateTime("@0");
    $dtT = new DateTime("@$seconds");
    return $dtF->diff($dtT)->format('%a jours, %h heures, %i minutes and %s secondes');
}


?>
