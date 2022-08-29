const completionSpec: Fig.Spec = {
    "name": "pypi",
    "description": "pypi",
    "subcommands": [
        {
            "name": "--help",
            "description": "获取帮助"
        },
        {
            "name": "upload",
            "description": "发布并提交到git",
            "args": [],
            "options": [
                {
                    "name": "-msg",
                    "description": "更新简要",
                    "args": {
                        "name": "msg",
                        "description": "更新简要",
                        "isVariadic": true
                    }
                }
            ]
        },
        {
            "name": "git-push",
            "description": "提交到git",
            "args": [],
            "options": [
                {
                    "name": "-msg",
                    "description": "提交简要",
                    "args": {
                        "name": "msg",
                        "description": "提交简要",
                        "isVariadic": true
                    }
                }
            ]
        },
        {
            "name": "post",
            "description": "在开发环境应用",
            "args": [
                {
                    "name": "path",
                    "description": "文件路径",
                    "template": [
                        "filepaths",
                        "folders"
                    ]
                }
            ],
            "options": []
        },
        {
            "name": "get",
            "description": "获取开发环境的文件",
            "args": [
                {
                    "name": "path",
                    "description": "文件路径",
                    "template": [
                        "filepaths",
                        "folders"
                    ]
                }
            ],
            "options": []
        },
        {
            "name": "gen-complete",
            "description": "为 Pypi Commander APP 生成自动补全脚本",
            "args": [
                {
                    "name": "--project_name",
                    "description": "项目名称",
                    "isOptional": true,
                    "args": {
                        "name": "project_name",
                        "description": "项目名称"
                    }
                }
            ],
            "options": []
        }
    ]
};
export default completionSpec;
