#!/usr/bin/env ruby
require 'net/http'
require 'uri'
###############
fver='6.4.8'
###############
def openurl(url)
  Net::HTTP.get(URI.parse(url))
end

puts "Version of this instance: " + fver.chomp

ver = openurl('http://ninth-destiny-mare.glitch.me/specsver')
if ver != fver
puts "██ Not up to date. Please update at https://github.com/aarikpokras/spectacleos. ██"
else
puts "██ spectacleOS is up to date. ██"
end

