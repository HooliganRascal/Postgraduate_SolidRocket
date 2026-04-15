import numpy as np
import matplotlib.pyplot as plt

# Basics
F=270e3; t=65; D=1.3; 
Isp=2550; rho=1.77e3; Tf=3373; gamma=11.4e-3; n=0.4;

# Grain Specifications
I=F*t;
m=I/Isp; v=m/rho; 

# Area of Chamber Section
rc=0.5*D; Ac=np.pi*rc*rc;

# Solve for Porting Area Ap by Best Suit Equation
a=np.pi*rc*rc; b=8.28*a; c=4*np.pi*rc*v;
M=1; N=-(2*a+b); P=a*a+2*a*b+c; Q=-a*a*b;

x=np.linspace(-2,2,100000);
y=M*x*x*x+N*x*x+P*x+Q;

i=1;
for i,y_val in enumerate(y):
    if np.abs(y_val)<1e-4:
        print(f'Index={i}, Ap={x[i]:.6f} m^2, y={y_val:.2e}');
        Ap=x[i];
        break;

A=Ac-Ap;
Lc=v/A;
Af=2*np.sqrt(Ap/np.pi)*Lc;
eta=A/Ac;
print(f'Area of Grain is {A} m^2, Area of Burning is {Af} m^2, Length of Chamber if {Lc} m, eta= {eta}');

plt.style.use('dark_background');
plt.figure(figsize=(10,6));
plt.plot(x,y,'cyan',linewidth=3);
plt.xlabel(r'$A_p/m^2$');
plt.ylabel(r'$F(A_p)$');
plt.title(r'Find $F(A_p)=0$');
plt.grid(True, alpha=0.2);
plt.show();

        
