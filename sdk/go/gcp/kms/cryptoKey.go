// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package kms

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// > This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/kms_crypto_key.html.markdown.
type CryptoKey struct {
	s *pulumi.ResourceState
}

// NewCryptoKey registers a new resource with the given unique name, arguments, and options.
func NewCryptoKey(ctx *pulumi.Context,
	name string, args *CryptoKeyArgs, opts ...pulumi.ResourceOpt) (*CryptoKey, error) {
	if args == nil || args.KeyRing == nil {
		return nil, errors.New("missing required argument 'KeyRing'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["keyRing"] = nil
		inputs["labels"] = nil
		inputs["name"] = nil
		inputs["purpose"] = nil
		inputs["rotationPeriod"] = nil
		inputs["versionTemplate"] = nil
	} else {
		inputs["keyRing"] = args.KeyRing
		inputs["labels"] = args.Labels
		inputs["name"] = args.Name
		inputs["purpose"] = args.Purpose
		inputs["rotationPeriod"] = args.RotationPeriod
		inputs["versionTemplate"] = args.VersionTemplate
	}
	inputs["selfLink"] = nil
	s, err := ctx.RegisterResource("gcp:kms/cryptoKey:CryptoKey", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &CryptoKey{s: s}, nil
}

// GetCryptoKey gets an existing CryptoKey resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetCryptoKey(ctx *pulumi.Context,
	name string, id pulumi.ID, state *CryptoKeyState, opts ...pulumi.ResourceOpt) (*CryptoKey, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["keyRing"] = state.KeyRing
		inputs["labels"] = state.Labels
		inputs["name"] = state.Name
		inputs["purpose"] = state.Purpose
		inputs["rotationPeriod"] = state.RotationPeriod
		inputs["selfLink"] = state.SelfLink
		inputs["versionTemplate"] = state.VersionTemplate
	}
	s, err := ctx.ReadResource("gcp:kms/cryptoKey:CryptoKey", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &CryptoKey{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *CryptoKey) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *CryptoKey) ID() *pulumi.IDOutput {
	return r.s.ID()
}

func (r *CryptoKey) KeyRing() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["keyRing"])
}

func (r *CryptoKey) Labels() *pulumi.MapOutput {
	return (*pulumi.MapOutput)(r.s.State["labels"])
}

func (r *CryptoKey) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

func (r *CryptoKey) Purpose() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["purpose"])
}

func (r *CryptoKey) RotationPeriod() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["rotationPeriod"])
}

func (r *CryptoKey) SelfLink() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["selfLink"])
}

func (r *CryptoKey) VersionTemplate() *pulumi.Output {
	return r.s.State["versionTemplate"]
}

// Input properties used for looking up and filtering CryptoKey resources.
type CryptoKeyState struct {
	KeyRing interface{}
	Labels interface{}
	Name interface{}
	Purpose interface{}
	RotationPeriod interface{}
	SelfLink interface{}
	VersionTemplate interface{}
}

// The set of arguments for constructing a CryptoKey resource.
type CryptoKeyArgs struct {
	KeyRing interface{}
	Labels interface{}
	Name interface{}
	Purpose interface{}
	RotationPeriod interface{}
	VersionTemplate interface{}
}
