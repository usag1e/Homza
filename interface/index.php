<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <link rel="stylesheet" type="text/css" href="assets/css/style.css">
    <title>Homza</title>
    <script>
        <?php 
        if ((substr($_SERVER['REMOTE_ADDR'],0,8) == "192.168.")) {
            echo 'var API_URL = "192.168.1.144"';
        } else if ($_SERVER['REMOTE_ADDR'] == "127.0.0.1") {
            echo 'var API_URL = "127.0.0.1"';
        } else {
            echo 'var API_URL = "70.82.148.225"';
        }
        ?>
    </script>
  </head>
  <body>
    <main id="content">
      <div
        v-if="home && home.name && home.background"
        title='SSID: {{ home.SSID }}\nPwd: {{ home.password }}'
        style="background-image: url('{{ home.background }}');"
        class='title-with-background'
      >
        <h1>{{ home.name }}</h1>
      </div>
      <h1 v-else>Welcome to your House</h1>
      <content>
        <user v-for='user in users'
          :name='user.value._id'
        >
        </user>
      </content>
      <content>
        <iss>
        </iss>
        <weather>
        </weather>
        <metro>
        </metro>
      </content>
    </main>
    <script src="dist/build.js"></script>
  </body>
</html>
