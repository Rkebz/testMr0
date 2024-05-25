require 'net/http'

def scan_server_and_ports(server, ports)
  begin
    addr = Socket.getaddrinfo(server, nil)
    sockaddr = Socket.pack_sockaddr_in(0, addr[0][3])
    s = Socket.new(Socket.const_get(addr[0][0]), Socket::SOCK_STREAM, 0)
    s.connect(sockaddr)
    puts "#{server}:#{ports} is open"
    s.close
  rescue
    puts "#{server}:#{ports} is closed"
  end
end

def check_user_info(url)
  uri = URI(url)
  http = Net::HTTP.new(uri.host, uri.port)
  request = Net::HTTP::Get.new(uri.request_uri)
  response = http.request(request)
  if response.code == '200'
    # Perform your checks on the user info
  else
    puts "Error fetching user info: #{response.code}"
  end
end

url = gets.chomp
server = 'example.com'
ports = [80, 443]
scan_server_and_ports(server, ports)
check_user_info(url)