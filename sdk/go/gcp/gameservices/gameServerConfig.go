// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package gameservices

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// A game server config resource. Configs are global and immutable.
//
// To get more information about GameServerConfig, see:
//
// * [API documentation](https://cloud.google.com/game-servers/docs/reference/rest/v1beta/projects.locations.gameServerDeployments.configs)
// * How-to Guides
//     * [Official Documentation](https://cloud.google.com/game-servers/docs)
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/game_services_game_server_config.html.markdown.
type GameServerConfig struct {
	pulumi.CustomResourceState

	// A unique id for the deployment config.
	ConfigId pulumi.StringOutput `pulumi:"configId"`
	// A unique id for the deployment.
	DeploymentId pulumi.StringOutput `pulumi:"deploymentId"`
	// The description of the game server config.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The fleet config contains list of fleet specs. In the Single Cloud, there will be only one.
	FleetConfigs GameServerConfigFleetConfigArrayOutput `pulumi:"fleetConfigs"`
	// The labels associated with this game server config. Each label is a key-value pair.
	Labels pulumi.StringMapOutput `pulumi:"labels"`
	// Location of the Deployment.
	Location pulumi.StringPtrOutput `pulumi:"location"`
	// The resource name of the game server config, in the form:
	// 'projects/{project_id}/locations/{location}/gameServerDeployments/{deployment_id}/configs/{config_id}'.
	Name pulumi.StringOutput `pulumi:"name"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringOutput `pulumi:"project"`
	// Optional. This contains the autoscaling settings.
	ScalingConfigs GameServerConfigScalingConfigArrayOutput `pulumi:"scalingConfigs"`
}

// NewGameServerConfig registers a new resource with the given unique name, arguments, and options.
func NewGameServerConfig(ctx *pulumi.Context,
	name string, args *GameServerConfigArgs, opts ...pulumi.ResourceOption) (*GameServerConfig, error) {
	if args == nil || args.ConfigId == nil {
		return nil, errors.New("missing required argument 'ConfigId'")
	}
	if args == nil || args.DeploymentId == nil {
		return nil, errors.New("missing required argument 'DeploymentId'")
	}
	if args == nil || args.FleetConfigs == nil {
		return nil, errors.New("missing required argument 'FleetConfigs'")
	}
	if args == nil {
		args = &GameServerConfigArgs{}
	}
	var resource GameServerConfig
	err := ctx.RegisterResource("gcp:gameservices/gameServerConfig:GameServerConfig", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetGameServerConfig gets an existing GameServerConfig resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetGameServerConfig(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *GameServerConfigState, opts ...pulumi.ResourceOption) (*GameServerConfig, error) {
	var resource GameServerConfig
	err := ctx.ReadResource("gcp:gameservices/gameServerConfig:GameServerConfig", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering GameServerConfig resources.
type gameServerConfigState struct {
	// A unique id for the deployment config.
	ConfigId *string `pulumi:"configId"`
	// A unique id for the deployment.
	DeploymentId *string `pulumi:"deploymentId"`
	// The description of the game server config.
	Description *string `pulumi:"description"`
	// The fleet config contains list of fleet specs. In the Single Cloud, there will be only one.
	FleetConfigs []GameServerConfigFleetConfig `pulumi:"fleetConfigs"`
	// The labels associated with this game server config. Each label is a key-value pair.
	Labels map[string]string `pulumi:"labels"`
	// Location of the Deployment.
	Location *string `pulumi:"location"`
	// The resource name of the game server config, in the form:
	// 'projects/{project_id}/locations/{location}/gameServerDeployments/{deployment_id}/configs/{config_id}'.
	Name *string `pulumi:"name"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project *string `pulumi:"project"`
	// Optional. This contains the autoscaling settings.
	ScalingConfigs []GameServerConfigScalingConfig `pulumi:"scalingConfigs"`
}

type GameServerConfigState struct {
	// A unique id for the deployment config.
	ConfigId pulumi.StringPtrInput
	// A unique id for the deployment.
	DeploymentId pulumi.StringPtrInput
	// The description of the game server config.
	Description pulumi.StringPtrInput
	// The fleet config contains list of fleet specs. In the Single Cloud, there will be only one.
	FleetConfigs GameServerConfigFleetConfigArrayInput
	// The labels associated with this game server config. Each label is a key-value pair.
	Labels pulumi.StringMapInput
	// Location of the Deployment.
	Location pulumi.StringPtrInput
	// The resource name of the game server config, in the form:
	// 'projects/{project_id}/locations/{location}/gameServerDeployments/{deployment_id}/configs/{config_id}'.
	Name pulumi.StringPtrInput
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringPtrInput
	// Optional. This contains the autoscaling settings.
	ScalingConfigs GameServerConfigScalingConfigArrayInput
}

func (GameServerConfigState) ElementType() reflect.Type {
	return reflect.TypeOf((*gameServerConfigState)(nil)).Elem()
}

type gameServerConfigArgs struct {
	// A unique id for the deployment config.
	ConfigId string `pulumi:"configId"`
	// A unique id for the deployment.
	DeploymentId string `pulumi:"deploymentId"`
	// The description of the game server config.
	Description *string `pulumi:"description"`
	// The fleet config contains list of fleet specs. In the Single Cloud, there will be only one.
	FleetConfigs []GameServerConfigFleetConfig `pulumi:"fleetConfigs"`
	// The labels associated with this game server config. Each label is a key-value pair.
	Labels map[string]string `pulumi:"labels"`
	// Location of the Deployment.
	Location *string `pulumi:"location"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project *string `pulumi:"project"`
	// Optional. This contains the autoscaling settings.
	ScalingConfigs []GameServerConfigScalingConfig `pulumi:"scalingConfigs"`
}

// The set of arguments for constructing a GameServerConfig resource.
type GameServerConfigArgs struct {
	// A unique id for the deployment config.
	ConfigId pulumi.StringInput
	// A unique id for the deployment.
	DeploymentId pulumi.StringInput
	// The description of the game server config.
	Description pulumi.StringPtrInput
	// The fleet config contains list of fleet specs. In the Single Cloud, there will be only one.
	FleetConfigs GameServerConfigFleetConfigArrayInput
	// The labels associated with this game server config. Each label is a key-value pair.
	Labels pulumi.StringMapInput
	// Location of the Deployment.
	Location pulumi.StringPtrInput
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringPtrInput
	// Optional. This contains the autoscaling settings.
	ScalingConfigs GameServerConfigScalingConfigArrayInput
}

func (GameServerConfigArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*gameServerConfigArgs)(nil)).Elem()
}
