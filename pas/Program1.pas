var x: integer;
begin
  x := 132;
  if x mod 2 = 0
  then
    Writeln('+++')
  else
    Writeln('---');
    
  Writeln(Odd(x));
end.