#!/usr/bin/perl -w
use Net::SFTP::Foreign;

my $sftp = Net::SFTP::Foreign->new('sarans01@dfwlnddeploy-01');
$sftp->die_on_error("Unable to establish SFTP connection");

$sftp->setcwd('/tmp') or die "unable to change cwd: " . $sftp->error;

$sftp->get("/tmp/test2.txt", "C:/Temp/test3.txt") or die "get failed: " . $sftp->error;
##get (from, To)


##put (local, remote)
#$sftp->put("C:/Temp/test2.txt", "/tmp/test2.txt") or die "put failed: " . $sftp->error;