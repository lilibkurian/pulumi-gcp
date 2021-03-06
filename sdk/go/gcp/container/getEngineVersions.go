// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package container

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides access to available Google Kubernetes Engine versions in a zone or region for a given project.
//
// > If you are using the `container.getEngineVersions` datasource with a
// regional cluster, ensure that you have provided a region as the `location` to
// the datasource. A region can have a different set of supported versions than
// its component zones, and not all zones in a region are guaranteed to
// support the same version.
func GetEngineVersions(ctx *pulumi.Context, args *GetEngineVersionsArgs, opts ...pulumi.InvokeOption) (*GetEngineVersionsResult, error) {
	var rv GetEngineVersionsResult
	err := ctx.Invoke("gcp:container/getEngineVersions:getEngineVersions", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getEngineVersions.
type GetEngineVersionsArgs struct {
	// The location (region or zone) to list versions for.
	// Must exactly match the location the cluster will be deployed in, or listed
	// versions may not be available. If `location`, `region`, and `zone` are not
	// specified, the provider-level zone must be set and is used instead.
	Location *string `pulumi:"location"`
	// ID of the project to list available cluster versions for. Should match the project the cluster will be deployed to.
	// Defaults to the project that the provider is authenticated with.
	Project *string `pulumi:"project"`
	// If provided, the provider will only return versions
	// that match the string prefix. For example, `1.11.` will match all `1.11` series
	// releases. Since this is just a string match, it's recommended that you append a
	// `.` after minor versions to ensure that prefixes such as `1.1` don't match
	// versions like `1.12.5-gke.10` accidentally. See [the docs on versioning schema](https://cloud.google.com/kubernetes-engine/versioning-and-upgrades#versioning_scheme)
	// for full details on how version strings are formatted.
	VersionPrefix *string `pulumi:"versionPrefix"`
}

// A collection of values returned by getEngineVersions.
type GetEngineVersionsResult struct {
	// Version of Kubernetes the service deploys by default.
	DefaultClusterVersion string `pulumi:"defaultClusterVersion"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// The latest version available in the given zone for use with master instances.
	LatestMasterVersion string `pulumi:"latestMasterVersion"`
	// The latest version available in the given zone for use with node instances.
	LatestNodeVersion string  `pulumi:"latestNodeVersion"`
	Location          *string `pulumi:"location"`
	Project           *string `pulumi:"project"`
	// A map from a release channel name to the channel's default version.
	ReleaseChannelDefaultVersion map[string]string `pulumi:"releaseChannelDefaultVersion"`
	// A list of versions available in the given zone for use with master instances.
	ValidMasterVersions []string `pulumi:"validMasterVersions"`
	// A list of versions available in the given zone for use with node instances.
	ValidNodeVersions []string `pulumi:"validNodeVersions"`
	VersionPrefix     *string  `pulumi:"versionPrefix"`
}
