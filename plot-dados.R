
x.ne = read.table("ne.txt")
x.nd = read.table("nd.txt")
x.eq = read.table("eq.txt")

time = 1:(dim(x.eq)[1])



png("output_ehrenfest.png", width = 600, height = 500)

plot(time,x.ne[,1],  type="l",col="blue" , cex = 0.8,
	ylim=range(x.ne[,1],x.nd[,1]),xlab="t",ylab="número de bolas" )
lines(time,x.nd[,1], type="l",col="red" )
lines(time,x.eq[,1], type="l",col="black" )

mtext( "Modelo de Urnas de Ehrenfest: Rota Irreversivel para o Equilibrio", side=3, cex=0.9, line=1)


legend("topright", bty="n",
       cex=1.0, seg.len = 1, lty=1, lwd=2,
       col=c("red","blue","black"), 
       legend =c("urna esquerda","urna direita","equilibrio") ) 
       
dev.off()

