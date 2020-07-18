setwd("~/Repo/ds4a-team75")
library("VGAM")
library("data.table")
library("ggplot2")
library(read)
datos <- read.csv("~/Repo/ds4a-team75/datos.csv")
datos<-as.data.table(datos)
m1<-vglm(NumberOT~ServiceType + District, family=posnegbinomial(), data=datos)
a=summary(m1)
a@predictors
names(a)

a@sigma

BD_fit<-data.frame(fitted(m1))
datos$predicted<-BD_fit[1]
#probability of more than one failure

datos$s2<-datos$predicted*(1+var(datos$NumberOT)*datos$predicted)
y=1
datos$prob_1<-(gamma(1/datos$s2+y)/(factorial(y)*gamma(1/datos$s2))*((1/datos$s2)^(1/datos$s2)*datos$predicted^(y)/(datos$predicted+(1/datos$s2))^((1/datos$s2)+y)))
y=2
datos$prob_2<-(gamma(1/datos$s2+y)/(factorial(y)*gamma(1/datos$s2))*((1/datos$s2)^(1/datos$s2)*datos$predicted^(y)/(datos$predicted+(1/datos$s2))^((1/datos$s2)+y)))
datos$prob12<-datos$prob_1+datos$prob_2

a=exp(resid(m1)[,1])
a

b=datos$NumberOT-datos$predicted

head(a)
head(b)

c=a-b
c=round(c,2)
c

output<-data.frame(resid=resid(m1)[,1], fitted=fitted(m1))
ggplot(output, aes(fitted,resid))+geom_jitter(position=position_jitter(width=0.25),
                                              alpha=0.5) + stat_smooth(method="loess")
resid(m1)


hist(fitted(m1))
hist(datos$NumberOT)

s2=var(datos[,"NumberOT"])
s2
y=50
mu=5
gamma(1/s2+y)/(factorial(y)*gamma(1/s2))*((1/s2)^(1/s2)*mu^(y)/(mu+(1/s2))^((1/s2)+y))

M<-npred(m1)
prplot(m1@fitted.values, lty = 1:M, col = (1:M)+2, rug = TRUE, las = 1,ylim = c(0, 1), rlwd = 2)
prplot(m1)
m1@fitted.values

log_munb<- -1.29758
log_size<- -2.02542
service_mantenerg<- -0.10657
distric_turbo<-0.35931

numb<-exp(log_munb)
size<-exp(log_size)

numb_full<-numb
media<-numb_full / (1 - (size / (size + numb_full))^size)
mediavars<-media+service_mantenerg + distric_turbo

a1=media
a2=media + service_mantenerg 
a3=media + distric_turbo
a4=media + distric_turbo + service_mantenerg
table(datos$predicted)


datos$prob50=dposnegbin(50,munb=datos$predicted, size=size)
datos$prob1=dposnegbin(1,munb=datos$predicted, size=size)





head(datos[District=="Turbo TyD",])

table(datos$predicted)

table(datos$ServiceType)

head(datos)
