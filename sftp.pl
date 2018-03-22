#!/usr/bin/perl -w

use Net::SFTP;

my $host = "dfwlnddeploy-01";
my %args = (
user => 'karots01',
password => 'Satish123',
debug => 'false'
);

my $sftp = Net::SFTP->new($host, %args);
print "connected!";

$sftp->put("C:/Temp/test2.txt", "/tmp/test2.txt");