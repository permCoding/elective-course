var x: integer;
begin
  var str := '12 66 34 45453 12';
  
  var arr := str.Split(' ');  
    
  Writeln(arr[0].ToInteger() + arr[1].ToInteger());
  
end.