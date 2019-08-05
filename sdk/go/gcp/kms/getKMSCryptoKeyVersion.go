// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package kms

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides access to a Google Cloud Platform KMS CryptoKeyVersion. For more information see
// [the official documentation](https://cloud.google.com/kms/docs/object-hierarchy#key_version)
// and
// [API](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions).
// 
// A CryptoKeyVersion represents an individual cryptographic key, and the associated key material.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/kms_crypto_key_version.html.markdown.
func LookupKMSCryptoKeyVersion(ctx *pulumi.Context, args *GetKMSCryptoKeyVersionArgs) (*GetKMSCryptoKeyVersionResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["cryptoKey"] = args.CryptoKey
		inputs["publicKey"] = args.PublicKey
		inputs["version"] = args.Version
	}
	outputs, err := ctx.Invoke("gcp:kms/getKMSCryptoKeyVersion:getKMSCryptoKeyVersion", inputs)
	if err != nil {
		return nil, err
	}
	return &GetKMSCryptoKeyVersionResult{
		Algorithm: outputs["algorithm"],
		CryptoKey: outputs["cryptoKey"],
		ProtectionLevel: outputs["protectionLevel"],
		PublicKey: outputs["publicKey"],
		State: outputs["state"],
		Version: outputs["version"],
		Id: outputs["id"],
	}, nil
}

// A collection of arguments for invoking getKMSCryptoKeyVersion.
type GetKMSCryptoKeyVersionArgs struct {
	// The `self_link` of the Google Cloud Platform CryptoKey to which the key version belongs.
	CryptoKey interface{}
	PublicKey interface{}
	// The version number for this CryptoKeyVersion. Defaults to `1`.
	Version interface{}
}

// A collection of values returned by getKMSCryptoKeyVersion.
type GetKMSCryptoKeyVersionResult struct {
	// The CryptoKeyVersionAlgorithm that this CryptoKeyVersion supports.
	Algorithm interface{}
	CryptoKey interface{}
	// The ProtectionLevel describing how crypto operations are performed with this CryptoKeyVersion. See the [protection_level reference](https://cloud.google.com/kms/docs/reference/rest/v1/ProtectionLevel) for possible outputs.
	ProtectionLevel interface{}
	// If the enclosing CryptoKey has purpose `ASYMMETRIC_SIGN` or `ASYMMETRIC_DECRYPT`, this block contains details about the public key associated to this CryptoKeyVersion. Structure is documented below.
	PublicKey interface{}
	// The current state of the CryptoKeyVersion. See the [state reference](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion.CryptoKeyVersionState) for possible outputs.
	State interface{}
	Version interface{}
	// id is the provider-assigned unique ID for this managed resource.
	Id interface{}
}