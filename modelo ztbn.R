#setting working directory
setwd("~/Repo/ds4a-team75")
#importing libraries
library("VGAM")
library("data.table")
library("ggplot2")
library("readxl")
library("xtable")
library( broom )
library(EnvStats)

#loading data
datos <- read.csv("~/Repo/ds4a-team75/datos.csv")
#converting data into data table
datos<-as.data.table(datos)
#identifying optimal transformation to data to identify outliers
a=boxcox(as.numeric(datos[["NumberOT"]]), optimize=TRUE)
l=a$lambda
#saving trasnformed data
datos[,"BC_NumberOT"] = (datos[,"NumberOT"]^(l) -1)/l
#using a boxplot to idenify outliers
b=boxplot(datos[,"BC_NumberOT"])
#filtering outliers
datosb<-datos[BC_NumberOT< b$stats[5],]


#fitting the positive negative binomial regression
m1<-vglm(NumberOT ~ c(ServiceType) + c(District) + as.factor(Month) +as.factor(weekday), family=posnegbinomial(), data=datosb)

#making plots of residuals vs fitted values an linear predictors mu, size
plot(m1)

#saving the main outputs related with the model
sm1=summary(m1)

#saving as a plain text the output of the model
sink("lm.png")
print(summary(m1))
sink() 


#fitting the positive poisson regression
m2 <- vglm(NumberOT ~ ServiceType + District + as.factor(Month) +as.factor(weekday), family = pospoisson(), data = datosb)
#saving the main outputs related with the model
sm2=summary(m2)

#extracting log a not log mean and size
logmunb<-sm1@coefficients[1]
logsize<-sm1@coefficients[2]
munb<-exp(logmunb)
size<-exp(logsize)

#adding a the predicted round counts
datosb$predicted<-data.frame(fitted(m1))
datosb$predict_round<- round(datosb$predicted,0)
#adding probablities of 1, 2, 3 or more than three failures
datosb$prob1<-dposnegbin(1, munb = datosb$predicted, size = size)
datosb$prob2<-dposnegbin(2, munb = datosb$predicted, size = size)
datosb$prob3<-dposnegbin(3, munb = datosb$predicted, size = size)
datosb$prob4<-dposnegbin(4, munb = datosb$predicted, size = size)
datosb$prob_may_3<-1-(datosb$prob1+datosb$prob2+datosb$prob3)
##I have doubts about the size...

#adding a the difference between predicted round counts and original counts
datosb$dif_pred<-datosb$NumberOT - datosb$predict_round
datosb$residuals<-data.frame(resid=resid(m1)[,1])




#adding the residual values to data
#datosb[,"resid_m1b"]<-data.frame(resid(m1b)[,1])

#making histograms of response variables and predicted values
#ggplot(datosb, aes(NumberOT))+
#  geom_histogram()
#ggplot(datosb, aes(predict_round))+
#  geom_histogram()
#ggplot(datosb, aes(predicted))+
#  geom_histogram()

###filtering strange data
datosb1<-datosb[abs(residuals)<6,]
########

####fitting the model without strange data
m1b<-vglm(NumberOT ~ c(ServiceType) + c(District) + as.factor(Month) +as.factor(weekday), family=posnegbinomial(), data=datosb1)
plot(m1b)

logmunb<-sm1@coefficients[1]
logsize<-sm1@coefficients[2]
munb<-exp(logmunb)
size<-exp(logsize)

#adding a the predicted round counts
datosb1$predicted<-data.frame(fitted(m1b))
datosb1$predict_round<- round(datosb$predicted,0)
#adding probablities of 1, 2, 3 or more than three failures
datosb1$prob1<-dposnegbin(1, munb = datosb$predicted, size = size)
datosb1$prob2<-dposnegbin(2, munb = datosb$predicted, size = size)
datosb1$prob3<-dposnegbin(3, munb = datosb$predicted, size = size)
datosb1$prob4<-dposnegbin(4, munb = datosb$predicted, size = size)
datosb1$prob_may_3<-1-(datosb$prob1+datosb$prob2+datosb$prob3)
#input data for plots
output<-data.frame(resid=resid(m1b)[,1], fitted=fitted(m1b))
#plot fitted vs resid
ggplot(output, aes(fitted,resid))+geom_jitter(position=position_jitter(width=0.25),
                                              alpha=0.5) + stat_smooth(method="loess")

#plot of fited vs resid with quantiles 
ggplot(output, aes(fitted,resid))+geom_jitter(position=position_jitter(width=0.25),
                                              alpha=0.5) + stat_quantile(method="rq")
#Data for fitted vs resid, sign bins of fitted
output <- within(output, {
  broken <- cut(fitted, hist(fitted, plot=FALSE)$breaks)
})

ggplot(output, aes(broken, resid))+
  geom_boxplot()+
  geom_jitter(alpha=0.25)

###reviewing for need of overdispersion parameter
(dLL<- 2*(logLik(m1)-logLik(m2)))

#comparing models to determine the need of overdispersion parameter
pchisq(dLL,df=1, lower.tail=FALSE)




#getting the mean and variance 
mean(datosb$NumberOT)
var(datosb$NumberOT)

mean(datosb$predict_round)
varfit=var(datosb$predict_round) + size
varfit

#coefi<-sm1@coefficients
#coefi<-coefi[3:length(coefi)]
#coefi

# calculating manually the value of the mean
#general_mean<-munb / (1 - (size / (size + munb))^size)
#general_mean

###plots of resulting probabilities of one failure by covariates
ggplot(datosb, aes(as.factor(Month), prob1, fill=District))+
  geom_boxplot()+
  xlab("Month")+
  ylab("Probability of one failure")+
  scale_fill_discrete(name = "District", labels = c("Apartadó TyD", "Turbo TyD"))


ggplot(datosb, aes(as.factor(Month), prob1, fill=ServiceType))+
  geom_boxplot()+
  xlab("Month")+
  ylab("Probability of one failure")+
  scale_fill_discrete(name = "Service type", labels = c("Energy damages", "Energy maintenance"))

###plots of resulting probabilities of two failures by covariates

ggplot(datosb, aes(as.factor(Month), prob2, fill=District))+
  geom_boxplot()+
  xlab("Month")+
  ylab("Probability of two failures")+
  scale_fill_discrete(name = "District", labels = c("Apartadó TyD", "Turbo TyD"))


ggplot(datosb, aes(as.factor(Month), prob2, fill=ServiceType))+
  geom_boxplot()+
  xlab("Month")+
  ylab("Probability of two failures")+
  scale_fill_discrete(name = "Service type", labels = c("Energy damages", "Energy maintenance"))

###plots of resulting probabilities of 3 failures by covariates
ggplot(datosb, aes(as.factor(Month), prob3, fill=District))+
  geom_boxplot()+
  xlab("Month")+
  ylab("Probability of three failures")+
  scale_fill_discrete(name = "District", labels = c("Apartadó TyD", "Turbo TyD"))


ggplot(datosb, aes(as.factor(Month), prob3, fill=ServiceType))+
  geom_boxplot()+
  xlab("Month")+
  ylab("Probability of three failures")+
  scale_fill_discrete(name = "Service type", labels = c("Energy damages", "Energy maintenance"))

###plots of resulting probabilities of more than 3 failures by covariates
ggplot(datosb, aes(as.factor(Month), prob_may_3, fill=District))+
  geom_boxplot()+
  xlab("Month")+
  ylab("Probability of more than three failures")+
  scale_fill_discrete(name = "District", labels = c("Apartadó TyD", "Turbo TyD"))


ggplot(datosb, aes(as.factor(Month), prob_may_3, fill=ServiceType))+
  geom_boxplot()+
  xlab("Month")+
  ylab("Probability of more than three failures")+
  scale_fill_discrete(name = "Service type", labels = c("Energy damages", "Energy maintenance"))

#testing the model with train and test data sets
train <- read.csv("~/Repo/ds4a-team75/train.csv")
datos<-as.data.table(train)

test <- read.csv("~/Repo/ds4a-team75/test.csv")
test<-as.data.table(test)

m1_train<-vglm(NumberOT ~ C(ServiceType) + C(District) + as.factor(Month), family=posnegbinomial(), data=train)
sm1_train=summary(m1_train)

predict(m1_train, newdata = test)

###printig data to plot in maps
write.csv(datosb1,"map_data.csv")






















