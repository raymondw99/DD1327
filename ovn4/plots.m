i  = 0
x0 = [10 100 1000 10000 100000 1000000];
y0 = [6e-6 8.8e-6 9e-6 6e-5 0.0006 0.008];
t0 = [0:10:1200000];
f0 = 1.3541e-9.*t0.*log10(t0);

x1 = [10 100 1000 10000 100000 1000000];
y1 = [1.2e-5 7.7e-5 0.0008 0.009 0.09 1];
t1 = [0:10:1200000];
f1 = 0.00000100133.*t1-0.002116;

x2 = [10 100 1000 10000 100000 1000000];
y2 = [1.9e-5 7.7e-5 0.0007 0.007 0.06 0.6];
t2 = [0:10:1200000];
f2 = 5.9975e-7*t2+0.00023416

if i == 0
    main(x0,y0,t0,f0,'Time for pow')
elseif i == 1
    main(x1,y1,t1,f1,'Time for sum1')
elseif i == 2
    main(x2,y2,t2,f2, 'Time for sum2')
end

function output = main(x,y,t,f,txt)
    plot(x,y,'*','LineWidth',10 ,'MarkerSize',5);
    xlabel('Elements (n)')
    ylabel('Time (s)')
    set(gcf,'color','w')
    title(txt)
    hold on;
    plot(t,f, 'b');
end
