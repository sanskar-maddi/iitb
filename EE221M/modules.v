module constant_int(
input [10:0] I, 
input [10:0] t, 
output reg [10:0] c);
real time_sec, Ic, factor, out;
integer charge;
always@(*)
begin
factor = 2.85e-4;
time_sec=t*60;
Ic=I;
out = Ic*time_sec*factor+10;
charge = out;
c = charge;
end
endmodule

//testbench
module tb_const();
reg [10:0] t,i;
wire [10:0] c;
constant_int c1(i,t,c);
initial
begin
#50
i = 3'b111; t = 16'b0000001010110010;
end
endmodule

module ramp_int(
input [10:0] a, 
input [10:0] t, 
output reg [10:0] c);
real time_sec, factor, out, slope;
integer charge;
always@(*)
begin
factor = 2.85e-4;
time_sec=t*60;
slope=a*1e-5;
out = (slope*time_sec*time_sec*factor/2)+10;
charge=out;
c=charge;
end
endmodule

//testbench
module tb_ramp();
reg [10:0] a,t;
wire [10:0] c;
ramp_int c1(a,t,c);
initial
begin
#50
a = 8'b00100001; 
t = 16'b0000001010110010;
end
endmodule

module exp_int(
input [10:0] beta, 
input [10:0] time_min, 
output reg [10:0] c);
real b, t, x, out, factor, I;
integer charge;
always@(*)
begin
I = 8;
factor = 2.85e-4;
b = beta*1e-5; t = time_min*60;
x = -(b*t);
out = (I*(5'd1 - $exp(x))/b)*factor;
charge = out;
c = charge;
end	
endmodule


module comp ( 
input [10:0] In1,
input [10:0] In2, 
output reg [10:0] t1,
output reg [10:0] t2);  
always @ (In1 or In2) 
begin 
     t1 = (In1 > In2)? (In1 - In2) : 1'b0;
     t2 = (In1 > In2)? In2 : In1;
end 
endmodule


module case_3(
input [10:0] b,
input [10:0] t,
input [10:0] t0,
input [10:0] I,
output reg [10:0] c);
wire [10:0] t1, t2, c1, c2;
comp C(t, t0, t1, t2);
exp_int E(b, t1, c1);
constant_int Ci(I, t2, c2);
always@(*)
begin
c = c1 + c2;
end

endmodule

//testbench
module tb();
reg [10:0] b, t, t0, I;
wire [10:0] c;
case_3 C1(b, t, t0, I, c);
initial
begin
b = 4'b1011; t = 10'b1010110010;
t0 = 9'b110110101; I = 4'b1000;
end
endmodule