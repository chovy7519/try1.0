/**
 * ========================================================================
 * === 项目配置文件 (config.js) ===
 * ========================================================================
 * * 未来您只需要修改这个文件中的内容，然后刷新 index.html 即可。
 * 请注意：
 * 1. 只修改 `"` 引号内的文本内容。
 * 2. `//` 后面的是注释，用于说明，不会显示在页面上。
 * 3. 数字（如面积、百分比）后面不要加引号。
 * */

const projectConfig = {

    // ===================================
    // 1. 园区基础信息 (可自定义)
    // ===================================
    parkName: "衡阳市农产品加工与绿色食品产业园",
    heroDescription: "基于衡阳市衡南县资源禀赋，构建科学、可量化的农产品加工与绿色食品产业发展路径。",
    totalAreaAcres: 3575, // 园区总用地面积 (亩) - 这个数字是计算的基准

    // ===================================
    // 2. 概览卡片 (可自定义)
    // ===================================
    overviewCards: [
        {
            title: "区位优势",
            text: "衡阳市衡南县，地处湘南交通枢纽，周边原料丰富，辐射长株潭城市群及粤港澳大湾区消费市场。"
        },
        {
            title: "规划面积",
            text: "总用地面积3575亩，分三期开发：近期350亩，中期1750亩，远期1475亩，形成梯度发展格局。"
        },
        {
            title: "产业体系",
            text: "聚焦油料（茶油）、粮食（大米）、畜禽、茶、中药材（土枇杷）五大特色产业，以及配套科研办公与冷链物流。"
        }
    ],

    // ===================================
    // 3. 核心经济系数 (可自定义)
    // ===================================
    economicFactors: {
        taxRate: 0.071,          // 总产值到总税收的折算系数 (例如: 0.071 对应 7.1%)
        jobFactor: 0.1,          // 亩均产值(万/亩)到就业的带动系数 (例如: 200万/亩 * 0.1 = 20人/亩)
        supportJobFactor: 0.5,   // 配套/科研类用地的亩均就业 (人/亩)
        taxTarget: 5,            // (可选) 经济效益分析中的税收目标 (亿元)
        jobTarget: 6000          // (可选) 经济效益分析中的就业目标 (人)
    },

    // ===================================
    // 4. 梯度发展阶段 (可自定义)
    // ===================================
    // - 您可以定义任意多个阶段
    // - `areaAcres`: 指 *该阶段* 的用地面积，非累计。
    // - `icon`: Font Awesome 图标 (例如: 'fa-flag', 'fa-industry', 'fa-rocket')
    // - `color`: 颜色 (例如: 'primary', 'secondary', 'accent')
    // - JS会自动计算 *累计* 产值、税收、就业并显示在对比图表中
    // - JS会自动计算 *该阶段* 产值、税收、就业并显示在时间轴卡片中
    // ===================================
    developmentStages: [
        {
            name: "近期",
            areaAcres: 350,
            years: "2025-2027",
            title: "基础筑基期",
            focus: "粮油加工",
            description: "搭建基础设施骨架，导入核心产业，形成'加工+物流'初步闭环。",
            icon: "fa-flag",
            color: "primary"
        },
        {
            name: "中期",
            areaAcres: 1750,
            years: "2027-2030",
            title: "规模扩张期",
            focus: "全产业链",
            description: "扩大产业规模，完善产业链中游，提升集聚效应。",
            icon: "fa-industry",
            color: "secondary"
        },
        {
            name: "远期",
            areaAcres: 1475,
            years: "2030-2035",
            title: "提质增效期",
            focus: "精深加工",
            description: "延伸高端环节，强化创新驱动，打造区域标杆。",
            icon: "fa-rocket",
            color: "accent"
        }
    ],

    // ===================================
    // 5. 产业板块与用地占比 (核心配置)
    // ===================================
    // - `key`: 唯一标识符 (英文)，勿重复
    // - `name`: 显示的名称
    // - `percent`: *默认* 用地占比 (%)
    // - `color`: 图表颜色
    // - `outputPerAcre`: 亩均产值 (万元/亩)。设为 0 表示非生产性用地 (如配套)
    // - `description`: 在滑块下方显示的简短描述
    // ===================================
    industries: [
        { key: 'grain-processing', name: '粮食加工', percent: 16, color: '#2E7D32', outputPerAcre: 135, description: '稻谷/大米精深加工' },
        { key: 'oil-processing', name: '油料加工', percent: 14, color: '#F9A825', outputPerAcre: 170, description: '茶油/油茶压榨及衍生品' },
        { key: 'tea-processing', name: '茶加工', percent: 14, color: '#1565C0', outputPerAcre: 200, description: '茶叶加工及茶食品开发' },
        { key: 'livestock-processing', name: '畜禽加工', percent: 11, color: '#4CAF50', outputPerAcre: 160, description: '畜禽屠宰及预制菜生产' },
        { key: 'herb-processing', name: '中药材加工', percent: 15, color: '#9C27B0', outputPerAcre: 190, description: '土枇杷等中药材提取' },
        { key: 'cold-logistics', name: '冷链物流', percent: 12, color: '#F44336', outputPerAcre: 100, description: '冷链仓储、运输、分拨等' },
        { key: 'research-office', name: '科研办公', percent: 10, color: '#FFC107', outputPerAcre: 0, description: '园区管理、研发、孵化、办公等' },
        { key: 'support-services', name: '配套服务', percent: 8, color: '#607D8B', outputPerAcre: 0, description: '生活、餐饮、住宿、能源等配套' }
    ],

    // ===================================
    // 6. 产业体系旭日图 (可自定义)
    // ===================================
    // 键(key)必须与 `industries` 中的 `key` 对应
    // ===================================
    industryChildren: {
        'grain-processing': [ { name: '稻谷精深加工', value: 1 }, { name: '大米制品', value: 1 } ],
        'oil-processing': [ { name: '茶油压榨', value: 1 }, { name: '油茶衍生品', value: 1 } ],
        'tea-processing': [ { name: '绿茶', value: 1 }, { name: '红茶', value: 1 }, { name: '茶食品', value: 1 } ],
        'livestock-processing': [ { name: '屠宰', value: 1 }, { name: '预制菜', value: 1 } ],
        'herb-processing': [ { name: '土枇杷提取', value: 1 }, { name: '保健品', value: 1 } ],
        'cold-logistics': [ { name: '仓储', value: 1 }, { name: '运输', value: 1 }, { name: '分拨', value: 1 } ],
        'research-office': [ { name: '研发', value: 1 }, { name: '孵化', value: 1 }, { name: '管理', value: 1 } ],
        'support-services': [ { name: '生活', value: 1 }, { name: '餐饮', value: 1 }, { name: '住宿', value: 1 } ]
    },

    // ===================================
    // 7. 页脚 (可自定义)
    // ===================================
    footer: {
        tagline: "推动农业现代化，构建绿色食品产业生态",
        copyright: "© 2025 同济设计城市与规划设计研究中心 保留所有权利."
    }
};