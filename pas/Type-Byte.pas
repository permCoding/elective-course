var a, b, c: byte;
begin
  a := 7; b := -2;
  if a > b
  then
    c := a
  else
    c := b;
  Writeln(c);
  // why is the answer 254 ?
end.