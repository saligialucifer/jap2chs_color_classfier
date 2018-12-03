rgb_1=textread('rgb.txt','%s');
rgb_2=textread('rgb_chs.txt','%s');
rgbs_jp=hex2rgb(rgb_1,256);
rgbs_chs=hex2rgb(rgb_2,256);
X=[rgbs_jp;rgbs_chs];
n_m= size(X,1);
Y = [ones(size(rgbs_jp,1),1);zeros(size(rgbs_chs,1),1)];
figure
x = X(:,1);
y = X(:,2);
z = X(:,3);
scatter3(x,y,z,100,Y);
SVMModel =  fitcsvm(X,Y,'ClassNames',[false true],'Standardize',true,...
        'KernelFunction','rbf','BoxConstraint',1); %训练分类器
CVSVMModel = crossval(SVMModel);   %分类器的交叉验证
classLoss = kfoldLoss(CVSVMModel); %  样本内错误率
[~,score] = predict(SVMModel,X)%;  %样本外的数据进行分类预测
[label,scorePred] = kfoldPredict(CVSVMModel); %样本外的数据进行分类预测结果，