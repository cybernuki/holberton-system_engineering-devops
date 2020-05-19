# Fixes bad 'phpp' extensions to 'php' in the WordPress file 'wp-settings.php'.

exec { 'fix':
    command  => 'sed -i "s|class-wp-locale.phpp|class-wp-locale.php|g" /var/www/html/wp-settings.php',
    provider => shell,
}
