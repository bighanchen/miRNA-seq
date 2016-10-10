library(survival)

TCGA_GBM_miRNA=read.table("TCGA_GBM_miRNA_microArray_level3_reverse_sel.txt", header=T)
time=TCGA_GBM_miRNA$time
status=TCGA_GBM_miRNA$status
rownames(TCGA_GBM_miRNA)=TCGA_GBM_miRNA$ID_REF
TCGA_GBM_miRNA=TCGA_GBM_miRNA[,c(-1,-536,-537)]

group=rep(1,487)

pvalue=matrix(data=-1,nr=534,nc=3)
i=1

mysurv=Surv(time,status)
for (miR in TCGA_GBM_miRNA)
{
	mycoxph=coxph(formula=mysurv ~ miR,TCGA_GBM_miRNA)
	sy=summary(mycoxph)
	thrhd=mean(miR)*sy$coefficients[1,1]
	pvalue[i,1]=sy$coefficients[1,1]
	pvalue[i,2]=sy$coefficients[1,5]
	group <- ifelse ((miR*sy$coefficients[1,1] >=thrhd), 0, 1)
	mydiff=survdiff(mysurv ~ group,rho=0)
	pvalue[i,3]=1-pchisq(mydiff$chisq,1)
	i=i+1
}
