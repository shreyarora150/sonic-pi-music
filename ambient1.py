live_loop :d2 do
  sample :ambi_glass_hum, amp: 3
  sleep 2
end

live_loop :d3 do
  sample :drum_heavy_kick, amp: 10, rate: 0.5
  sleep 0.3
  sample :drum_heavy_kick, amp: 10, rate: 0.5
  sleep 1
  sample :drum_cymbal_pedal, amp: 10
  sleep 1
end

live_loop :g do
  sample :guit_e_fifths, amp: 5
  sleep 1
end

live_loop :e do
  sample :guit_harmonics  , amp: 5
  sleep 2
end


live_loop :d1 do
  
  play :A4
  sleep 0.4
  play :E5
  sleep 0.4
  play :A5
  sleep 0.4
  play :Db6
  sleep 0.4
  play :A5
  sleep 0.4
  play :E5
  sleep 0.4
  
  play :A4
  sleep 0.4
  play :E5
  sleep 0.4
  play :A5
  sleep 0.4
  play :Db6
  sleep 0.4
  play :A5
  sleep 0.4
  play :E5
  sleep 0.4
  
  play :D4
  sleep 0.4
  play :A4
  sleep 0.4
  play :D5
  sleep 0.4
  play :Gb5
  sleep 0.4
  play :D5
  sleep 0.4
  play :A4
  sleep 0.4
  
  play :D4
  sleep 0.4
  play :A4
  sleep 0.4
  play :D5
  sleep 0.4
  play :Gb5
  sleep 0.4
  play :D5
  sleep 0.4
  play :A4
  sleep 0.4
  
end