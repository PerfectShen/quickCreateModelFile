//
//  TestModel.h
//
//
//  Created by fl-226 on 27/2/2019.
//  Copyright © 2019年 fl-226. All rights reserved.
//


#import <Foundation/Foundation.h>

@interface TestModel : NSObject


//sssss
@property (nonatomic, copy) NSString *userpic

//用户ID
@property (nonatomic, strong) NSNumber *userid

//标题
@property (nonatomic, copy) NSString *title

//小视频id
@property (nonatomic, strong) NSNumber *videoid

//小视频url
@property (nonatomic, copy) NSString *videoUrl

//小视频封面地址
@property (nonatomic, copy) NSString *videoCover

//小视频动图封面地址
@property (nonatomic, copy) NSString *dynamicCover

//小视频长度
@property (nonatomic, strong) NSNumber *time

//直播状态 1 直播中，0直播结束
@property (nonatomic, strong) NSNumber *livestatus

//roomid
@property (nonatomic, strong) NSNumber *roomid

//城市
@property (nonatomic, strong) NSNumber *city

//0-不在线 1-在线
@property (nonatomic, strong) NSNumber *onlinestatus

//点赞数
@property (nonatomic, strong) NSNumber *praisecount

//评论数
@property (nonatomic, strong) NSNumber *commentcount

//分享数
@property (nonatomic, strong) NSNumber *sharecount

//礼物数
@property (nonatomic, strong) NSNumber *giftcount

//音乐来源人ID
@property (nonatomic, strong) NSNumber *sourceaudiouserid

//音乐来源人头像
@property (nonatomic, copy) NSString *sourceaudiouserpic

//音乐ID
@property (nonatomic, strong) NSNumber *audioid

//是否点赞 0没有 1已点赞
@property (nonatomic, strong) NSNumber *ispraise


@end