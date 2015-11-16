<?php
	require_once 'lib/couch.php';
	require_once 'lib/couchClient.php';
	require_once 'lib/couchDocument.php';
	require_once 'lib/dataAccess.php';

	$view_last_seen = last_seen();
	$view_house = get_printer_status();
	
include('includes/header.php');
// echo "<meta http-equiv='refresh' content='30;url=.'>";
	
?><!DOCTYPE html>
<html>
	<head>
	
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes"/>
        <link href="assets/css/icon.css" rel="stylesheet" type="text/css">
        <link href="assets/css/style.css" rel="stylesheet" type="text/css">
	</head>
	
<body>
    <div id="page">
      <div>
        <p>
    <?php
      echo "SSID : DORMATORY" ;
      echo "&nbsp;&nbsp;&nbsp;&nbsp;";
      echo " Pwd : 43JEAN87BRILLANT";
    ?>	
        </p>  
      </div>
      <div>
        <h2> Who's UP ? </h2><br />
        <div id='who'>
        <?php
          
          foreach ( $view_last_seen->rows as $row){
            echo '<div class="img_container">';
            $date =  $row->key;
            $url_img =  $row->value[1];
            $name = $row->value[0];
            $nowdate = time();
            $timestamp = strtotime($date);
            $word = $row->value;
            $seen_since = $nowdate - $timestamp;
            $nowDate = gmdate("Y-m-d H:i", $nowdate);
            $lastSeenDate = date("Y-m-d H:i", strtotime($date));
            if ($seen_since < 300){
              echo '<div class="img_in" title="'.$name.'" style="background-image:url('.$url_img.')"></div>';	
              echo '<div>In da House !</div><div>Since :</div>';
              echo '<div class="small">( '.secondsToTime($seen_since).' )';
            }elseif ($seen_since < 900){
              echo '<div class="img_just" title="'.$name.'" style="background-image:url('.$url_img.')"></div>';
              echo '<div>Should be around ... (last seen less than 15 minutes ago)';
            }else {
              echo '<div class="img_out" title="'.$name.'" style="background-image:url('.$url_img.')"></div>';
              echo '<div>Out !</div>';
              echo '<div>Last seen:</div>';
              echo '<div class="small">'.secondsToTime($seen_since).' ago</div>';
              echo '<div class="small">( '.$lastSeenDate.' )';
            }
            echo '</div>'; // Closing 'Last seen'
            echo '</div>'; // Closing container
          }		
        ?>
      </div>
    </div>
	<div>
		<h2> Weather </h2><br />
			<?php
				$json = "http://127.0.0.1:5984/house_status/Weather";
				$jsonfile = file_get_contents($json);

				$weather = json_decode($jsonfile);
        echo '<img src="http://openweathermap.org/img/w/', $weather->icon, '.png">';
				echo '<h3>', $weather->state, '</h3>';
				echo 'Temperature is : ' , $weather->temperature, ' Celsius <br />';
				echo 'Pressure is : ' , $weather->pressure,'<br />';
			?>
			
	</div>		
	<div>
	<h2> Octoprint </h2><br />

			<?php
				$json = "http://127.0.0.1:5984/house_status/_design/list/_view/printer";
				$jsonfile = file_get_contents($json);
		$printer_json = json_decode($jsonfile);
				echo ' <b>Printer is currently </b> :  ', $printer_json->rows[0]->value->printer_status;
				echo '<br /> <b>Head temperature</b> :  ', $printer_json->rows[0]->value->head_temperature;
				echo '<br /> <b>Bed temperature</b> :  ', $printer_json->rows[0]->value->bed_temperature;
				echo '<br /> <b>Job name </b> : ', $printer_json->rows[0]->value->job_name;
				
			?>
			
    	
    
	</div>
</div>
</body>
</html>
