import React, { Component } from "react";
import { Link } from "react-router-dom";
import { Menu, Layout } from "antd";
import type { MenuProps } from "antd";

import "./styles.scss";

const { Sider, Content } = Layout;

interface ProfileSettingsSideNavPropsInterface {
    path: string;
}

export class ProfileSettingsSideNav extends Component<ProfileSettingsSideNavPropsInterface, unknown> {
    path = this.props.path;

    items: MenuProps["items"] = [
        {
            key: "1",
            label: <h2 className="m-5 text-estela-black-medium text-base">ACCOUNT SETTINGS</h2>,
            children: [
                {
                    key: "profile",
                    label: (
                        <Content className="pl-2 flex items-center stroke-black hover:stroke-estela hover:bg-button-hover hover:text-estela rounded">
                            <Link to={`/settings/profile`}>Profile</Link>
                        </Content>
                    ),
                },
                {
                    key: "password",
                    label: (
                        <Content className="pl-2 flex items-center stroke-black hover:stroke-estela hover:bg-button-hover hover:text-estela rounded">
                            <Link to={`/settings/password`}>Password</Link>
                        </Content>
                    ),
                },
            ],
            type: "group",
        },
        {
            key: "2",
            label: <h2 className="m-5  text-estela-black-medium text-base">PROJECTS SETTINGS</h2>,
            children: [
                {
                    key: "dataPersistence",
                    label: (
                        <Content className="pl-2 flex items-center hover:bg-button-hover stroke-black hover:stroke-estela rounded">
                            <Link to={`/settings/dataPersistence`}>Data persistence</Link>
                        </Content>
                    ),
                },
            ],
            type: "group",
        },
    ];

    render(): JSX.Element {
        return (
            <Sider width={240}>
                <Menu items={this.items} mode="inline" className="h-full" selectedKeys={[`${this.path}`]} />
            </Sider>
        );
    }
}
